import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
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
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью.</b>!",
        parse_mode=ParseMode.HTML
    )


@dp.message(F.text)
async def all_message(message: Message):
    await message.answer(
        "Введите команду /start, чтобы начать общение.",
        parse_mode=ParseMode.HTML
    )


if __name__ == "__main__":
    asyncio.run(main())
