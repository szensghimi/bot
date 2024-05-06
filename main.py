import asyncio


from aiogram import Bot, Dispatcher
from handlers import main_handlers
from environs import Env

env = Env()
env.read_env()

async def on_startup():
    print("bot started...")


# Функция конфигурирования и запуска бота
async def main() -> None:


    # Инициализируем бот и диспетчер
    bot = Bot(token=env("BOT_TOKEN")) 
    dp = Dispatcher()


    # Регистриуем роутеры в диспетчере
    dp.include_router(main_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await on_startup()

asyncio.run(main())