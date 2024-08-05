import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup

TG_API_TOKEN = ''
dp = Dispatcher(storage=MemoryStorage())

class UserState(StatesGroup):
    address = State()

async def main():
    bot = Bot(token=TG_API_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да")
    kb.button(text="Нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_information_and_start_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.buttons(text="Информация")
    kb.button(text="Начало")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_inline_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Информация',
            callback_data='info')
    )
    print(builder.buttons)
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def start(message: Message):
    #await message.answer("Привет!", reply_markup=get_information_and_start_buttons())
    await message.answer("Привет!", reply_markup=get_inline_buttons())

@dp.callback_query(F.data == "info")
async def information(call):
    await call.message.answer('Информация о боте')
    await call.answer() #Завершение вызова кнопки

@dp.message(F.text == "Информация")
async def button_information(message: Message):
    await message.answer(
        "Информация!",
        parse_mode=ParseMode.HTML
    )

@dp.message(F.text == "Начало")
async def button_start(message: Message):
    await message.answer(
        "Начало!",
        parse_mode=ParseMode.HTML
    )

@dp.message(Command(commands='Заказать'), StateFilter(default_state))
async def buy(message: Message,
              state: FSMContext):
    await message.answer(
        "Отправь свой адрес, пожалуйста",
        parse_mode=ParseMode.HTML
    )
    await state.set_state(UserState.address)

@dp.message(StateFilter(UserState.address), F.text.isalpha())
async def address_handler(message: Message,
                         state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f'Доставка заказа будет отправлена на {data['address']}')

if __name__ == "__main__":
    asyncio.run(main())
