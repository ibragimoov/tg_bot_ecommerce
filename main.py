import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

from app.database.models import async_main


async def main():
    bot = Bot(token='8101609114:AAGEMmGwCm3m-SQ70jYQwVtayd2N8Wk0qBY')
    dp = Dispatcher()
    dp.include_router(router)
    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    print('Бот запущен')
    asyncio.run(main())

#1 вспомнить код
#2 узнать, что такое бд
#3 как использовать бд + питон
#4 практика