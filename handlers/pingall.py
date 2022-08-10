from aiogram import types
from pyrogram import types

from misc import dp, app


@dp.message_handler(lambda m: m.chat.type in ["group", "supergroup"], commands=["pingall"])
async def pingall_cmd(message: types.Message):
    arg = message.get_args() #аргумент з функції

    users = [user async for user in app.get_chat_members(message.chat.id)] #список користувачів
    
    for user in users: #перебір користувачів чату
        user: types.ChatMember
        if not user.user.is_deleted or not user.user.is_bot:  #відбір справжніх користувачів
            arg += f'<a href="tg://user?id={user.user.id}">\u2060</a>' #додаємо пінг в аргумент
    
    await message.answer(
        arg
    )


