import asyncio
import aiohttp
import logging

FORMAT = "[%(asctime)s][%(name)s][%(process)d %(processName)s][%(levelname)-8s] %(funcName)-8s: %(message)s"
logging.basicConfig(format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


async def main() -> None:
    """Run simple test."""
    LOG.debug("Test health endpoint")
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:5430/health") as resp:
            assert resp.status == 200, "HTTP Status code error"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
