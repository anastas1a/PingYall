from aiogram import types

from misc import dp
from utils import get_members


@dp.message_handler(commands=["kickdeads"])
async def kickdeads_cmd(message: types.message):
    if message.chat.type not in ["group", "supergroup"]:
        return await message.answer(
            "Цією командою можна користуватися тільки в групових чатах!"
        )
        
    if not (await message.chat.get_member(message.from_user.id)).status in ["creator", "administrator"]:
        return await message.answer(
            "Цією командою можуть користуватися лише адміністратори!"
        )

    if not (await message.chat.get_member(message.bot.id))["can_restrict_members"]:
        return await message.answer(
            "Я не можу видаляти користувачів без прав адміністратора!"
        )

    dead_members = await get_members(message.chat.id, lambda member: member.user.is_deleted) #видалені користувачі

    n = 0 
    for dead_member in dead_members: #видалення
        try:
            await message.chat.kick(dead_member.user.id)
            n += 1
        except Exception as e:
            print(e)

    await message.answer(
        f"Кікнуто <code>{n}</code> видалених акаунтів ☠️"
    )