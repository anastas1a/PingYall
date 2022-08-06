from aiogram import types

from misc import dp


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Привіт! Я бот тагал.")

