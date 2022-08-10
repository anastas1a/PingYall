from aiogram import types
from misc import dp

@dp.message_handler(commands=["pinginfo"])
async def pinginfo_cmd(message: types.message):
    await message.answer("Інформація")