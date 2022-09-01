from aiogram import types
from misc import dp

@dp.message_handler(commands=["help"])
async def help_cmd(message: types.message):
    await message.answer(
        "Доступні команди:\n"
        "\n"
        "/start —  початок роботи зі мною.\n"
        "/help — опис доступних команд.\n"
        "/pingall —  тегнути усіх користувачів в чаті смайлами.\n"
        "/pingall + <i>ваш текст</i> —  тегнути користувачів в чаті вашим текстом.\n"
        "/kickdeads — кікнути видалені акаунти в чаті."
    )
