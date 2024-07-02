from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.filter import Myfilter

class Home:
    router = Router(name=__name__)
    
    @router.message(CommandStart())
    async def start(self, message: Message) -> None:
        await message.answer('Hello ASYNio!')
    
    @router.message(Myfilter('hello'))
    async def hello(self, message: Message) -> None:
        await message.answer('Hello User!')
    
    async def example_test(self):
        return 'test'
