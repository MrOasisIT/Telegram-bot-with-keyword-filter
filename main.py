from aiogram import Bot,Dispatcher
import asyncio
from handlers.pacrer import router
import logging
import os
from dotenv import load_dotenv

load_dotenv()

log = logging.getLogger(__name__)

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

TOKEN = os.getenv("TOKEN")

async def main():
    if not TOKEN:
        log.error("Токен не найден в .env")
        return
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        log.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception:
        await bot.session.close()
        log.exception("Бот приостановил работу из-за ошибки")
    finally:
        await bot.session.close()
        log.info("Бот приостановил работу")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt,SystemExit):
        log.info("Бот приостановлен администратором")
    except Exception:
        log.exception("Произошла ошибка при созданий цикла событий")

