from aiogram.filters import Filter
from aiogram.types import Message

class Myfilter(Filter):
    def __init__(self, text: str):
       self.text = text
    
    async def __call__(self, message: Message) -> bool:
        return message.text == self.text 