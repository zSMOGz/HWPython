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
BUTTON_BUY_URL = "https://www.bybit.com/"
BUTTON_BACK = "Назад"
BUTTON_BACK_CALL = "back_to_catalog"

BUTTON_USERS = "Пользователи"
BUTTON_USERS_CALL = "users"
BUTTON_STATS = "Статистика"
BUTTON_STATS_CALL = "stats"
BUTTON_BLOCKS = "Блокировка"
BUTTON_BLOCKS_CALL = "block"
BUTTON_UNBLOCKS = "Разблокировка"
BUTTON_UNBLOCKS_CALL = "unblock"

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
        [InlineKeyboardButton(text=BUTTON_BUY, url=BUTTON_BUY_URL)],
        [InlineKeyboardButton(text=BUTTON_BACK, callback_data=BUTTON_BACK_CALL)]
    ], resize_keyboard=True
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=BUTTON_USERS, callback_data=BUTTON_USERS_CALL)],
        [InlineKeyboardButton(text=BUTTON_STATS, callback_data=BUTTON_STATS_CALL)],
        [
            InlineKeyboardButton(text=BUTTON_BLOCKS, callback_data=BUTTON_BLOCKS_CALL),
            InlineKeyboardButton(text=BUTTON_UNBLOCKS, callback_data=BUTTON_UNBLOCKS_CALL)
        ]
    ], resize_keyboard=True
)