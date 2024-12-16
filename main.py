import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '8042152535:AAEDZceviCGCJC2HuCPjKuCOprYecajKoGg'

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):

    kb = [
        [KeyboardButton(text='Чудово')],
        [KeyboardButton(text='Погано')]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer('HELLO! I am a bot!')
    await message.answer('Як справи ?', reply_markup=keyboard)


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Help message')

@dp.message()
async def catch_message(message: types.Message):


    if message.text.lower() == 'чудово':
        await message.answer('Дуже гарно!')

    elif message.text.lower() == 'погано':
        await message.answer('Шкода!')

async def main():
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


