from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardButton

BUTTON_COST = "Стоимость"
BUTTON_ABOUT = "О нас"

BUTTON_GAME_M = "Маленькая игра"
BUTTON_GAME_M_CALL = "small"
BUTTON_GAME_L = "Средняя игра"
BUTTON_GAME_L_CALL = "medium"
BUTTON_GAME_XL = "Большая игра"
BUTTON_GAME_XL_CALL = "big"
BUTTON_OTHER = "Другие предложения"
BUTTON_OTHER_CALL = "other"

BUTTON_BUY = "Купить"
BUTTON_BUY_URL = "https://www.bybit.com/trade/usdt/XRPUSDT"

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BUTTON_COST),
            KeyboardButton(text=BUTTON_ABOUT)
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=BUTTON_GAME_M, callback_data=BUTTON_GAME_M_CALL)],
        [InlineKeyboardButton(text=BUTTON_GAME_L, callback_data=BUTTON_GAME_L_CALL)],
        [InlineKeyboardButton(text=BUTTON_GAME_XL, callback_data=BUTTON_GAME_XL_CALL)],
        [InlineKeyboardButton(text=BUTTON_OTHER, callback_data=BUTTON_OTHER_CALL)]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=BUTTON_BUY, url=BUTTON_BUY_URL)]
    ], resize_keyboard=True
)
