from misc import app
from pyrogram import types, enums

from config import USERS_CHUNK_SIZE
import random


async def get_user_tag_list(chat_id: int):
    users = [f"<a href='tg://user?id={member.user.id}'>\u2060</a>" async for member in app.get_chat_members(chat_id)] #список користувачів
    return [users[i:i + USERS_CHUNK_SIZE] for i in range(0, len(users), USERS_CHUNK_SIZE)]

