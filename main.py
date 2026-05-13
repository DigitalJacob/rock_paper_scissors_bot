import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from config.config import Config, load_config
from handlers import commands, game, buttons, unknown
from logger.setup import setup_logging, get_logger, user_log_info

async def main() -> None:
    config: Config = load_config()

    setup_logging(
        level=config.log.level,
        log_file="bot.log",
        console_output=True
    )

    logger = get_logger(__name__)
    logger.info("Запуск бота")

    session = AiohttpSession(proxy=config.proxy.url)
    logger.info(f"Подключен прокси: {config.proxy.type}://{config.proxy.ip}:{config.proxy.port}")

    bot = Bot(token=config.bot.token, session=session)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(buttons.router)
    dp.include_router(game.router)
    dp.include_router(unknown.router)
    logger.info("Роутеры зарегистрированы")

    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Webhook удалён")

    logger.info("Бот настроен и начинает работу")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")
    except Exception as e:
        logging.error(f"Критическая ошибка: {e}", exc_info=True)