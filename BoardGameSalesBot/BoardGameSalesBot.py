import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

import keyboards as k
import texts as t

dp = Dispatcher(storage=MemoryStorage())


async def main():
    bot = Bot(token=t.c.TG_API_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(t.START, reply_markup=k.start_kb)


@dp.message(F.text == k.BUTTON_COST)
async def price(message: Message):
    await message.answer(t.PRICE, reply_markup=k.catalog_kb)


@dp.message(F.text == k.BUTTON_ABOUT)
async def about(message: Message):
    await message.answer(t.ABOUT, reply_markup=k.start_kb)


@dp.callback_query(F.data == k.BUTTON_GAME_M_CALL)
async def buy_m(call):
    await call.message.answer(t.M_GAME, reply_markup=k.buy_kb)
    await call.answer()


@dp.callback_query(F.data == k.BUTTON_GAME_L_CALL)
async def buy_l(call):
    await call.message.answer(t.L_GAME, reply_markup=k.buy_kb)
    await call.answer()


@dp.callback_query(F.data == k.BUTTON_GAME_XL_CALL)
async def buy_xl(call):
    await call.message.answer(t.XL_GAME, reply_markup=k.buy_kb)
    await call.answer()


@dp.callback_query(F.data == k.BUTTON_OTHER)
async def buy_other(call):
    await call.message.answer(t.OTHER, reply_markup=k.buy_kb)
    await call.answer()


if __name__ == "__main__":
    asyncio.run(main())
