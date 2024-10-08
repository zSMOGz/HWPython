import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

TG_API_TOKEN = 'TOKEN'
dp = Dispatcher(storage=MemoryStorage())


async def main():
    bot = Bot(token=TG_API_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью!")


@dp.message(F.text)
async def all_message(message: Message):
    print("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    asyncio.run(main())
