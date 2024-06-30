import os

from dotenv import load_dotenv
from aiogram import Bot

# Load ENV file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Bot conn
bot = Bot(os.getenv('TOKEN'))

