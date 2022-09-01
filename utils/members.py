from misc import app
from typing import Callable


async def get_members(chat_id: int, filter: Callable = None, chunk: int = None):
    members = [member async for member in app.get_chat_members(chat_id) if filter is None or filter(member)]
    if chunk:
        members = [members[i:i + chunk] for i in range(0, len(members), chunk)]

    return members
