import asyncio

from misc import dp, app
from aiogram import executor
from config import TOKEN

import handlers


async def start_up(dp):
    await app.start(bot_token=TOKEN)

executor.start_polling(dp, on_startup=start_up)

