import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Привет, введите название фильма, который вы хотите скачать")



@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text="Wait a second...",
    )
  


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token = "6345228761:AAF4TFu4L-aKWzX1wenqQ1W4eUW0hFrgOhs")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())