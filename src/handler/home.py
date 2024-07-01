from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.filter import Myfilter

class Home:
    router = Router(name=__name__)
    
    @router.message(CommandStart())
    async def start(message: Message) -> None:
        await message.answer('Hello ASYNio!')
    
    @router.message(Myfilter('hello'))
    async def start(message: Message) -> None:
        await message.answer('Hello User!')
