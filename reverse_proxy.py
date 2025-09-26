import sys
import aiohttp
import asyncio
import aiohttp.web_request
from aiohttp import web
from urllib.parse import urljoin, urlparse


TARGET = "https://player.vidinfra.com"
REFERER = 'https://biologyadda.com/'
COOKIE = None
PORT = 5000


HOST = urlparse(TARGET).hostname


def regenerateCookies(text: str, *args):
    for i in args: text += f';{i}'
    def __format(k: str):
        a, b = k.split('=', 1)
        return f'{a.strip()}={b.strip()}'
    return ';'.join(map(__format, filter(lambda x: bool(x.strip()), text.split(';'))))

def replaceAbsoluteURLs(text:str, prHost:str, ssl:bool = False):
    s = 's' if ssl else ''
    return text \
            .replace('ws://' + HOST, f'ws{s}://' + prHost) \
            .replace('wss://' + HOST, f'ws{s}://' + prHost) \
            .replace('http://' + HOST, f'http{s}://' + prHost) \
            .replace('https://' + HOST, f'http{s}://' + prHost) 

async def handle_request(request : aiohttp.web_request.Request):
    if \
        'websocket' in request.headers.get('Upgrade', '').lower() \
        or 'upgrade' in request.headers.get('Connection', '').lower() \
        or request.headers.get('Sec-WebSocket-Key') \
        or request.headers.get('Sec-WebSocket-Accept') \
        or request.headers.get('Sec-WebSocket-Version') \
        or request.headers.get('Sec-WebSocket-Protocol') \
        or request.headers.get('Sec-WebSocket-Extensions') \
        : return await handle_websocket(request)
    
    method = request.method
    path = request.rel_url.path_qs
    target_url = urljoin(TARGET, path)
    ssl = request.headers.get('X-Forwarded-Proto', request.scheme).endswith('s')

    proxyHost = request.headers.get('Host', HOST)
    headers = {k.lower() : v for k, v in request.headers.items() if k.lower() not in ['host', 'accept-encoding']}
    headers['accept-encoding'] = 'identity'

    headers['cookie'] = regenerateCookies(headers.get('cookie', ''), COOKIE or '')

    if k := headers.get('referer'): headers['referer'] = k.replace(proxyHost, HOST)
    if k := headers.get('origin'): headers['origin'] = k.replace(proxyHost, HOST)
    if REFERER: headers['referer'] = REFERER

    async def body_generator():
        async for chunk in request.content.iter_chunked(3e6):
            yield chunk

    async with aiohttp.ClientSession() as s:
        async with s.request(method, target_url, headers=headers, data=body_generator() if request.can_read_body else None, timeout=60, allow_redirects=False, ssl=False) as r:
            reqHeaders = r.headers.copy()
            ctype = reqHeaders.get('Content-Type', '')
            if loc := reqHeaders.get('Location'):
                del reqHeaders['Location']
                reqHeaders['Location'] = replaceAbsoluteURLs(loc, proxyHost, ssl)
            sr = web.StreamResponse(
                status=r.status,
                headers={k: v for k, v in r.headers.items() if k.lower() not in ["transfer-encoding", "content-length", "connection", "content-encoding"]}
            )
            await sr.prepare(request)

            if True in [i in ctype for i in ['text/html', 'application/javascript', 'text/javascript', 'text/xml']]:
                respText = await r.text('utf-8')
                # print(respText)
                if 'just a moment' in respText.lower():
                    await sr.write("Cloudflare Blocked this request. Need Verification")
                else:
                    await sr.write(replaceAbsoluteURLs(respText, proxyHost, ssl).encode(errors='ignore'))
            else:
                async for chunk in r.content.iter_chunked(5e6):
                    await sr.write(chunk)

            await sr.write_eof()
            return sr


async def handle_websocket(request : aiohttp.web_request.Request):
    path = request.rel_url.path_qs
    target_url = urljoin(TARGET, path).replace('http', 'ws')

    ws_server = web.WebSocketResponse()
    await ws_server.prepare(request)

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(target_url, ssl=False) as ws_client:
            async def ws_forward(reader, writer):
                async for msg in reader:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        await writer.send_str(msg.data)
                    elif msg.type == aiohttp.WSMsgType.BINARY:
                        await writer.send_bytes(msg.data)
                    elif msg.type == aiohttp.WSMsgType.CLOSE:
                        await writer.close()

            await asyncio.gather(
                ws_forward(ws_server, ws_client),
                ws_forward(ws_client, ws_server)
            )

    return ws_server


app = web.Application()
app.router.add_route('*', '/{tail:.*}', handle_request)

if __name__ == '__main__':
    for i in sys.argv[1:]:
        k, v = i.split('=', 1)
        globals()[k.strip()] = v.strip()

    print('Running server with:')
    print('TARGET:', TARGET)
    print('COOKIE:', COOKIE)
    print('PORT:', PORT)
    web.run_app(app, port=int(PORT))
