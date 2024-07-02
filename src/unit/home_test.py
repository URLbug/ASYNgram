import unittest
import asyncio

from unittest.mock import AsyncMock

from ..handler import home

class Home_Test(unittest.TestCase):
    def test_home(self):
        test = home.Home()

        message_mock = AsyncMock(text='hello')

        self.assertEqual(asyncio.run(test.example_test()), 'test')
        self.assertEqual(asyncio.run(test.hello(message_mock)), None)