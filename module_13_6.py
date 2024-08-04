import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

TG_API_TOKEN = 'TOKEN'
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def main():
    bot = Bot(token=TG_API_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def get_norma_and_formula() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Рассчитать норму калорий',
            callback_data='calories'),
        InlineKeyboardButton(
            text='Формулы расчёта',
            callback_data='formulas')
    )
    print(builder.buttons)
    return builder.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!", reply_markup=get_norma_and_formula())


@dp.callback_query(F.data == "calories")
async def information(call,
                      state):
    await call.message.answer("Введите свой возраст:")
    await call.answer()  # Завершение вызова кнопки
    await state.set_state(UserState.age)


@dp.callback_query(F.data == "formulas")
async def information(call):
    await call.message.answer(' 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()  # Завершение вызова кнопки


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
