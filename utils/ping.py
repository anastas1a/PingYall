from misc import app
from config import USERS_CHUNK_SIZE

async def get_user_tag_list(chat_id: int):
    users = [f"<a href='tg://user?id={user.user.id}'>\u2060</a>" async for user in app.get_chat_members(chat_id)] #список користувачів
    return [users[i:i + USERS_CHUNK_SIZE] for i in range(0, len(users), USERS_CHUNK_SIZE)]


