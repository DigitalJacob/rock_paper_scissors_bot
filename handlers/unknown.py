from aiogram.types import Message
from aiogram import Router

from lexicon.lexicon_ru import UNKNOWN_COMMAND_TEXT, UNKNOWN_COMMAND_WITH_GAME
from storage.user_data import is_game_active
from keyboards.game_keyboard import get_game_keyboard
from keyboards.start_keyboard import get_start_keyboard
from logger.setup import get_logger, user_log_info


router = Router()
logger = get_logger(__name__)

@router.message()
async def process_unknown_message(message: Message):
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: отправил неподходящее сообщение")

    user_id = message.from_user.id

    if not is_game_active(user_id):
        await message.answer(
            text=UNKNOWN_COMMAND_TEXT,
            reply_markup=get_start_keyboard()
        )
        return
    await message.answer(
        text=UNKNOWN_COMMAND_WITH_GAME,
        reply_markup=get_game_keyboard()
    )