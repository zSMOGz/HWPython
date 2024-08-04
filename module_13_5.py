import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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

def get_calories_and_information_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рассчитать")
    kb.button(text="Информация")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!", reply_markup=get_calories_and_information_buttons())

@dp.message(F.text == "Информация")
async def button_information(message: Message):
    await message.answer(
        "Информация",
        parse_mode=ParseMode.HTML
    )

@dp.message(F.text == "Рассчитать")
async def button_calories(message: Message,
                          state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)

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
