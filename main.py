import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import logging
from wikipedia import PageError, wikipedia

BOT_TOKEN = '7762937649:AAGba6BVFMtN7krrr061EsGmZtSVLmoYI54'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Welcome to my Wiki_bot. Send any word : ")

@dp.message(Command('help'))
async def help_(message: Message):
    await message.answer('If you need any help, just ask from user @adxam04!!!')

@dp.message()
async def get_wiki_info(message: Message):
    try:
        await message.reply(wikipedia.summary(message.text))
    except PageError:
        await message.reply("WORD NOT FOUND!!!")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

