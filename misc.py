from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from config import TOKEN


bot = Bot(TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())
