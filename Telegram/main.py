#Импортируем все необходимые модули
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#импортируем созданные ранее файлы
from config import *
from keyboards import *
import texts

#--------------------------------------------------------#
#Ваш API токен
api = API
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
    #--------------------------------------------------------#

#обработчик кнопок
#Декоратор обработки текстового сообщения "Привет"
@dp.message_handler(commands = ['Am1801012Artem'])
async def special_message(message: types.Message):
    await message.answer('Ссылка на код', reply_markup = code)
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup = start_kb)
@dp.message_handler(Text(equals=['О нас']))
async def send_info(message):
    await message.answer(texts.about_as, parse_mode = 'HTML', reply_markup = O_nas  )
@dp.message_handler(Text(equals=['РАЗМЕРЫ']))
async def send_price_list(message):
    await message.answer('<b>Выберите интересующую вас размер</b>', parse_mode = 'HTML', reply_markup = catalog_kb)
@dp.message_handler(Text(equals=['Поддержка']))
async def send_price_list(message):
    await message.answer('Помощь команде', parse_mode = 'HTML', reply_markup = Donat)
@dp.callback_query_handler(text='Маленькая кормушка')
async def manikur(call):
    await call.message.answer(texts.mk, parse_mode = 'HTML', reply_markup = buy_kb)
@dp.callback_query_handler(text='Стандарт')
async def pedikur(call):
    await call.message.answer(texts.s, parse_mode = 'HTML', reply_markup = buy_kb)
@dp.callback_query_handler(text='Большая кормушка')
async def narast(call):
    await call.message.answer(texts.bk, parse_mode = 'HTML', reply_markup = buy_kb)
@dp.callback_query_handler(text='Свой размер')
async def other(call):
    await call.message.answer(texts.other, parse_mode = 'HTML', reply_markup = buy_kb1)
@dp.callback_query_handler(text='Назад')
async def manikur(call):
    await call.message.answer('<b>Выберите интересующую вас услугу</b>', parse_mode = 'HTML', reply_markup = catalog_kb)
@dp.callback_query_handler(text='Оплата')
async def narast(call):
    await call.message.answer(texts.bk1, parse_mode = 'HTML', reply_markup = buy_kb1)
@dp.callback_query_handler(text='Купить')
async def narast(call):
    await call.message.answer(texts.bk1, parse_mode = 'HTML', reply_markup = buy_kb1)
@dp.callback_query_handler(text='Наш бусти')
async def other(call):
    await call.message.answer(texts.other, parse_mode = 'HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)