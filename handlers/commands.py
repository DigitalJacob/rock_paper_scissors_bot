from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import Command, CommandStart

from keyboards.game_keyboard import get_game_keyboard
from keyboards.start_keyboard import get_start_keyboard
from logger.setup import get_logger, user_log_info
from lexicon.lexicon_ru import (
    HELP_COMMAND_TEXT, START_COMMAND_TEXT, CANCEL_MESSAGE, NO_ACTIVE_GAME_MESSAGE,
)
from storage.user_data import set_game_state, is_game_active, get_user_data


router = Router()
logger = get_logger(__name__)

@router.message(CommandStart())
async def process_start_command(message: Message):
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: команда /start")

    await message.answer(
        text=START_COMMAND_TEXT,
        reply_markup=get_start_keyboard(),
    )

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: команда /help")

    user_id = message.from_user.id
    current_keyboard = get_game_keyboard() if is_game_active(user_id) else get_start_keyboard()

    await message.answer(
        text=HELP_COMMAND_TEXT,
        reply_markup=current_keyboard,
    )

@router.message(F.text == 'Статистика')
@router.message(Command(commands='stat'))
async def process_stat_command(message: Message) -> None:
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: запрос статистики")

    user_id = message.from_user.id
    stats = get_user_data(user_id).stats

    if stats.total_games == 0:
        await message.answer(NO_ACTIVE_GAME_MESSAGE, reply_markup=get_start_keyboard())
        return

    win_rate = (stats.wins / stats.total_games * 100) if stats.total_games > 0 else 0

    await message.answer(
        f"Ваша статистика\n\n"
        f"🎮 Всего матчей: {stats.total_games}\n"
        f"🏆 Побед: {stats.wins}\n"
        f"💀 Поражений: {stats.losses}\n"
        f"📈 Процент побед: {win_rate:.1f}%",
        reply_markup=get_start_keyboard()
    )

@router.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: отмена игры")

    user_id = message.from_user.id
    if is_game_active(user_id):
        set_game_state(user_id, False)
        await message.answer(
            CANCEL_MESSAGE,
            reply_markup=get_start_keyboard()
        )
    else:
        await message.answer(
            NO_ACTIVE_GAME_MESSAGE,
            reply_markup=get_start_keyboard()
        )
