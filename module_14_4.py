import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, FSInputFile, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from crud_functions import *

TG_API_TOKEN = ''
BUTTON_CALCULATE = "Рассчитать"
BUTTON_INFO = "Информация"
BUTTON_BUY = "Купить"
BUTTON_PRODUCT1 = "Продукт1"
BUTTON_PRODUCT2 = "Продукт2"
BUTTON_PRODUCT3 = "Продукт3"
BUTTON_PRODUCT4 = "Продукт4"
BUTTON_PRODUCT_CALL = "product_buying"
ANSWER_BUY_PRODUCT = "Выберите продукт для покупки:"
BUY_SUCCESS_CALL = "buying_success"

dp = Dispatcher(storage=MemoryStorage())
products = Products()
all_products = products.get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def main():
    bot = Bot(token=TG_API_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def get_calories_and_information_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=BUTTON_CALCULATE)
    kb.button(text=BUTTON_INFO)
    kb.button(text=BUTTON_BUY)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=BUTTON_PRODUCT1, callback_data=BUTTON_PRODUCT_CALL),
         InlineKeyboardButton(text=BUTTON_PRODUCT2, callback_data=BUTTON_PRODUCT_CALL),
         InlineKeyboardButton(text=BUTTON_PRODUCT3, callback_data=BUTTON_PRODUCT_CALL),
         InlineKeyboardButton(text=BUTTON_PRODUCT4, callback_data=BUTTON_PRODUCT_CALL)]
    ], resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!", reply_markup=get_calories_and_information_buttons())


@dp.message(F.text == BUTTON_CALCULATE)
async def button_calories(message: Message,
                          state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(F.text == BUTTON_INFO)
async def button_information(message: Message):
    await message.answer(BUTTON_INFO)


@dp.message(F.text == BUTTON_BUY)
async def price(message: Message):
    await get_buying_list(message)


async def get_buying_list(message: Message):
    for product in all_products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        path = f'images/img_({product[4]}).jpg'
        await message.answer_photo(photo=FSInputFile(path))
    await message.answer(ANSWER_BUY_PRODUCT, reply_markup=catalog_kb)


@dp.callback_query(F.data == BUTTON_PRODUCT_CALL)
async def buy_m(call):
    await send_confirm_message(call)
    await call.answer()


@dp.callback_query(F.data == BUTTON_PRODUCT_CALL)
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message(StateFilter(UserState.age), F.text.isdigit())
async def set_growth(message: Message,
                     state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(StateFilter(UserState.growth), F.text.isdigit())
async def set_growth(message: Message,
                     state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(StateFilter(UserState.weight), F.text.isdigit())
async def send_calories(message: Message,
                        state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    norm_of_colors = (10 * float(data['weight'])
                      + 6.25 * int(data['growth'])
                      - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий {norm_of_colors}')
    await state.set_state(default_state)


if __name__ == "__main__":
    asyncio.run(main())
