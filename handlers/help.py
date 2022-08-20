from aiogram import types
from misc import dp

@dp.message_handler(commands=["help"])
async def hel_cmd(message: types.message):
    await message.answer(
        "/start —  початок роботи зі мною.\n" 
        "/pingall —  тегнути усіх користувачів в чаті смайлами.\n"
        "/pingall <i>ваш текст</i> —  тегнути користувачів в чаті вашим текстом."
    )
