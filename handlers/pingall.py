from aiogram import types
from pyrogram import types

import random
from misc import dp
from utils import get_members

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

    members_chunk = await get_members(message.chat.id, lambda member: not (member.user.is_bot or member.user.is_deleted), chunk=5)

    generate = not bool(arg)
    for members in members_chunk:
        if generate:
            arg = ''.join(random.sample(EMOJI_LIST, len(members)))

        await message.answer(
            arg +  "".join([f"<a href='tg://user?id={member.user.id}'>\u2060</a>" for member in members])
        )
        
