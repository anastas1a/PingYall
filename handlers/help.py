from aiogram import types
from misc import dp

@dp.message_handler(commands=["help"])
async def hel_cmd(message: types.message):
    await message.answer(
        "Доступні команди:\n"
        "\n"
        "/start —  початок роботи зі мною.\n"
        "/help — опис доступних команд.\n"
        "/pingall —  тегнути усіх користувачів в чаті смайлами.\n"
        "/pingonline — тегнути тільки тих користувачів, які онлайн.\n"
        "/pingall або /pingonline + <i>ваш текст</i> —  тегнути користувачів в чаті вашим текстом.\n"
    )
