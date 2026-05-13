from aiogram import Router, F
from aiogram.types import Message

from storage.user_data import set_game_state, reset_game_scores
from keyboards.game_keyboard import get_game_keyboard
from keyboards.start_keyboard import get_start_keyboard
from logger.setup import get_logger, user_log_info
from lexicon.lexicon_ru import (
    AGREE_BUTTON_TEXT, DISAGREE_BUTTON_TEXT, GAME_START_MESSAGE, DISAGREE_TEXT
)


router = Router()
logger = get_logger(__name__)

@router.message(F.text == AGREE_BUTTON_TEXT)
async def process_agree_button(message: Message) -> None:
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: начал игру")

    user_id = message.from_user.id

    # Начинаем новую игру
    set_game_state(user_id, True)
    reset_game_scores(user_id)  # обнуляем счёт

    await message.answer(
        text=GAME_START_MESSAGE,
        reply_markup=get_game_keyboard()
    )

@router.message(F.text == DISAGREE_BUTTON_TEXT)
async def process_disagree_button(message: Message):
    user_info = user_log_info(message.from_user)
    logger.info(f"{user_info}: отказался играть")

    await message.answer(
        DISAGREE_TEXT,
        reply_markup=get_start_keyboard()
    )