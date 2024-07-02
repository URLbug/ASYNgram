import unittest
import asyncio

from unittest.mock import AsyncMock

from src.handler import home

class Home_Test(unittest.TestCase):
    def test_home(self):
        message_mock = AsyncMock(text='/start')

        self.assertEqual(asyncio.run(home.Home.hello(message_mock)), None)