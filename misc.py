from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from telethon import TelegramClient

from config import TOKEN


bot = Bot(TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())

app = TelegramClient(
    "stuff/pingyallsess", 
    6, 
    "eb06d4abfb49dc3eeb1aeb98ae0f581e"
)
