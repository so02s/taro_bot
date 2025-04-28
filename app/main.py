import asyncio
from aiogram import Bot, Dispatcher
from decouple import config
from handlers import router

bot = Bot(token=config("BOT_TOKEN"))

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())