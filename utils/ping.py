from misc import app
from telethon import types

from config import USERS_CHUNK_SIZE
import random


async def get_user_tag_list(chat_id: int):
    users = [f"<a href='tg://user?id={member.id}'>\u2060</a>" async for member in app.iter_participants(chat_id) if not (member.deleted or member.bot or member.is_self)] #список користувачів
    return [users[i:i + USERS_CHUNK_SIZE] for i in range(0, len(users), USERS_CHUNK_SIZE)]
