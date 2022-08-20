from aiogram import types
from pyrogram import types

from misc import dp
from utils import get_user_tag_list


@dp.message_handler(lambda m: m.chat.type in ["group", "supergroup"], commands=["pingall"])
async def pingall_cmd(message: types.Message):
    arg = message.get_args() #аргумент з функції
    users_tag_list = await get_user_tag_list(message.chat.id)

    for users in users_tag_list:
        await message.answer(
            arg +  "".join(users)
        )
        