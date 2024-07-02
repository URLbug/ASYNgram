from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.filter import Myfilter
from src.database import Test

class Home:
    router = Router(name=__name__)
    
    @router.message(CommandStart())
    async def start(message: Message) -> None:
        await Test().create(id=2)

        await message.answer('Hello ASYNio!')
    
    @router.message(Myfilter('hello'))
    async def hello(message: Message) -> None:
        await message.answer('Hello User!')
