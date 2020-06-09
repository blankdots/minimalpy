from aiohttp import web
import logging
import asyncio
import uvloop

FORMAT = '[%(asctime)s][%(name)s][%(process)d %(processName)s][%(levelname)-8s] (L:%(lineno)s) %(funcName)s: %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

routes = web.RouteTableDef()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


@routes.get('/health')
async def healthcheck(request: web.Request) -> web.Response:
    """Test health, will always return ok."""
    LOG.debug('Healthcheck called')
    return web.Response(body='OK')


async def init() -> web.Application:
    """Initialise server."""
    server = web.Application()
    server.router.add_routes(routes)
    return server


def main():
    """Do the server."""
    host = '0.0.0.0'  # nosec
    port = 5430

    LOG.info(f"Started server on {host}:{port}")
    web.run_app(init(), host=host, port=port, shutdown_timeout=0)


if __name__ == '__main__':
    main()
