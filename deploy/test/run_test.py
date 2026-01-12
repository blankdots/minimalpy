import asyncio
import aiohttp
import logging

FORMAT = "[%(asctime)s][%(name)s][%(process)d %(processName)s][%(levelname)-8s] %(funcName)-8s: %(message)s"
logging.basicConfig(format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

MAX_RETRIES = 30
RETRY_DELAY = 1.0


async def wait_for_server(session: aiohttp.ClientSession, url: str) -> None:
    """Wait for server to be ready with retries."""
    for attempt in range(MAX_RETRIES):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=2)) as resp:
                if resp.status == 200:
                    LOG.debug(f"Server is ready after {attempt + 1} attempt(s)")
                    return
                LOG.debug(f"Server returned status {resp.status}, retrying...")
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            LOG.debug(f"Attempt {attempt + 1}/{MAX_RETRIES}: Server not ready yet: {e}")
            if attempt < MAX_RETRIES - 1:
                await asyncio.sleep(RETRY_DELAY)
            else:
                raise
    raise RuntimeError(f"Server did not become ready after {MAX_RETRIES} attempts")


async def main() -> None:
    """Run simple test."""
    LOG.debug("Test health endpoint")
    async with aiohttp.ClientSession() as session:
        await wait_for_server(session, "http://localhost:5430/health")
        async with session.get("http://localhost:5430/health") as resp:
            assert resp.status == 200, "HTTP Status code error"


if __name__ == "__main__":
    asyncio.run(main())
