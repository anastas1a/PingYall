from aiogram import types

from misc import dp


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(
        "<b>Слава Україні! 🇺🇦 </b>\n"
        "\n"
        "Я бот PingYall і мене створили для того, щоб допомогти тобі в одну мить зібрати всіх людей в твоєму чаті!\n"
        "\n"
        "ℹ️ <i>Якщо ти хочеш дізнатися більше про те, як я працюю, використовуй команду /pinginfo</i>"
    )

