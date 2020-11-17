from typing import Awaitable
import unittest
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from minimalpy.server import init, main
from unittest import mock


class AppTestCase(AioHTTPTestCase):
    """Test for Web app.

    Testing web app endpoints.
    """

    async def get_application(self) -> Awaitable:
        """Retrieve web Application for test."""
        return await init()

    @unittest_run_loop
    async def test_health(self) -> None:
        """Simplest test the health endpoint."""
        resp = await self.client.request("GET", "/health")
        assert 200 == resp.status
        assert "OK" == await resp.text()


class TestBasicFunctionsApp(unittest.TestCase):
    """Test App Base.

    Testing basic functions from web app.
    """

    def setUp(self) -> None:
        """Initialise fixtures."""
        pass

    def tearDown(self) -> None:
        """Remove setup variables."""
        pass

    @mock.patch("minimalpy.server.web")
    def test_main(self, mock_webapp) -> None:
        """Should start the webapp."""
        main()
        mock_webapp.run_app.assert_called()

    async def test_init(self) -> None:
        """Test init type."""
        server = await init()
        self.assertIs(type(server), web.Application)


if __name__ == "__main__":
    unittest.main()
