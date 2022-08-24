from aiogram import types
from pyrogram import types

import random
from misc import dp
from utils import get_user_tag_list, get_user_online_tag_list

EMOJI_LIST = ["🇺🇦", "🔵", "🟡", "💛", "💙", "🟨", "🟦"]


@dp.message_handler(commands=["pingall"])
async def pingall_cmd(message: types.Message):
    if message.chat.type not in ["group", "supergroup"]:
        return await message.answer(
            "Цією командою можна користуватися тільки в групових чатах!"
        )
        
    arg = message.get_args() #аргумент з функції
    if not (await message.bot.get_chat_member(message.chat.id, message.from_user.id)).status in ["creator", "administrator"]:
        return await message.answer(
            "Цією командою можуть користуватися лише адміністратори!"
        )

    users_tag_list = await get_user_tag_list(message.chat.id)

    generate = not bool(arg)
    for users in users_tag_list:
        if generate:
            arg = ''.join(random.sample(EMOJI_LIST, len(users)))

        await message.answer(
            arg +  "".join(users)
        )
        
@dp.message_handler(commands=["pingonline"])
async def pingonline_cmd(message: types.Message):
    if message.chat.type not in ["group", "supergroup"]:
        return await message.answer(
            "Цією командою можна користуватися тільки в групових чатах!"
        )
        
    arg = message.get_args() #аргумент з функції
    if not (await message.bot.get_chat_member(message.chat.id, message.from_user.id)).status in ["creator", "administrator"]:
        return await message.answer(
            "Цією командою можуть користуватися лише адміністратори!"
        )

    users_tag_list = await get_user_online_tag_list(message.chat.id)
    generate = not bool(arg)
    for users in users_tag_list:
        if generate:
            arg = ''.join(random.sample(EMOJI_LIST, len(users)))

        await message.answer(
            arg +  "".join(users)
        )
        