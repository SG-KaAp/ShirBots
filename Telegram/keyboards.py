from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'РАЗМЕРЫ'),
            KeyboardButton(text = 'Поддержка'),
            KeyboardButton(text = 'О нас')
        ],
    ],resize_keyboard=True
)
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Маленькая кормушка', callback_data = 'Маленькая кормушка'),
        ],
        [
            InlineKeyboardButton(text = 'Стандарт', callback_data = 'Стандарт'),
        ],
        [
            InlineKeyboardButton(text = 'Большая кормушка', callback_data = 'Большая кормушка'),
        ],
        [
            InlineKeyboardButton(text = 'Свой размер', callback_data = 'Свой размер'),
        ],
    ]
)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оплата", callback_data = 'Оплата'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data = 'Назад'),
        ],
    ]
)

buy_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать мененджеру", url='t.me/Yuitfdd'),
        ],
    ]
)
O_nas = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data = 'Назад'),
        ],
        [
            InlineKeyboardButton(text="Написать мененджеру", url='t.me/Yuitfdd'),
        ],
    ]
)
Donat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш бусти", url='https://boosty.to/teremkrluvokrela/donate'),
        ],
    ]
)
code = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="github", url='https://github.com/SG-KaAp/ShirBots'),
        ],
    ]
)