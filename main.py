import asyncio
from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from handlers import router

bot = Bot(token=config("BOT_TOKEN"))
redis_url = config('REDIS_URL')
storage = RedisStorage.from_url(config('REDIS_URL'))

async def main():
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

