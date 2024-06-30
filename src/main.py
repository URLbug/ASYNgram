import logging
import asyncio

from aiogram import Dispatcher

from __init__ import bot

import sys

sys.path.append('..')

from handler import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def main() -> None:
    dp = Dispatcher()

    dp.include_routers(Home.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
