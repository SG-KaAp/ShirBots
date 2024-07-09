import configparser
import texts
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

config = configparser.ConfigParser()
config.read('config.ini')

vk_api_token = config['VK_api']['api_token']
group_id = config['VK_api']['group_id']
vk = Bot(vk_api_token, group_id)

@vk.on.private_message(text=['Ку', 'Привет', 'Меню', 'Начать', 'Назад'])
async def menu(message: Message):
    await message.answer(
        message = texts.start,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('РАЗМЕРЫ'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('Поддержка'), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text('ℹ️ О нас'), color=KeyboardButtonColor.PRIMARY)
        )
    )
@vk.on.private_message(text=['ℹ️ О нас'])
async def about_us(message: Message):
    await message.answer(
        message = texts.about_as,
    )
@vk.on.private_message(text=['РАЗМЕРЫ'])
async def scales(message: Message):
    await message.answer(
        message = texts.start,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Маленькая кормушка'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('Стандарт'), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text('Большая кормушка'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('Свой размер'), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text('Назад'), color=KeyboardButtonColor.NEGATIVE)
        )
    )
@vk.on.private_message(text=['Маленькая кормушка'])
async def mk(message: Message):
    await message.answer(
        message = texts.mk,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Оплата'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Назад'), color=KeyboardButtonColor.NEGATIVE)
        )
    )
@vk.on.private_message(text=['Стандарт'])
async def s(message: Message):
    await message.answer(
        message = texts.s,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Оплата'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Назад'), color=KeyboardButtonColor.NEGATIVE)
        )
    )
@vk.on.private_message(text=['Большая кормушка'])
async def bk(message: Message):
    await message.answer(
        message = texts.mk,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Оплата'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Назад'), color=KeyboardButtonColor.NEGATIVE)
        )
    )
@vk.on.private_message(text=['Свой размер'])
async def other(message: Message):
    await message.answer(
        message = texts.other,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Оплата'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Назад'), color=KeyboardButtonColor.NEGATIVE)
        )
    )
@vk.on.private_message(text=['Поддержка'])
async def donate(message: Message):
    await message.answer(
        message = 'Наш бусти: https://boosty.to/teremkrluvokrela/donate',
    )
@vk.on.private_message(text=['Оплата'])
async def buy(message: Message):
    await message.answer(
        message=texts.bk1,
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('РАЗМЕРЫ'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('Поддержка'), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text('ℹ️ О нас'), color=KeyboardButtonColor.PRIMARY)
        )
    )
vk.run_forever()
