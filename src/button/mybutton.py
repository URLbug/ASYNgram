from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

class Mybutton:
   def inline(self) -> InlineKeyboardMarkup:
       build = InlineKeyboardBuilder()

       build.button(text="Home", callback_data="home")

       return build.as_markup()

   def reply(self) -> ReplyKeyboardMarkup:
       build = ReplyKeyboardBuilder()

       build.button("Home")

       return build.as_markup()
