from aiogram import F, Router
from aiogram.types import Message
from random import choice

from keyboards.game_keyboard import get_game_keyboard
from keyboards.start_keyboard import get_start_keyboard
from logger.setup import get_logger, user_log_info
from services.game_logic import determine_winner
from lexicon.lexicon_ru import (
    WIN_ROUND_MESSAGE, LOSE_ROUND_MESSAGE, TIE_ROUND_MESSAGE,
    MATCH_WIN_MESSAGE, MATCH_LOSE_MESSAGE, NO_ACTIVE_GAME_MESSAGE,
    CHOOSE_OPTION_MESSAGE,
)
from storage.user_data import (
    is_game_active, set_game_state, update_game_score,
    update_stats, reset_game_scores
)


GAME_OPTIONS = ('🪨', '✂️', '📄')
TARGET_SCORE = 3  # До 3 побед
ROUND_MESSAGES = {
    'win': WIN_ROUND_MESSAGE,
    'lose': LOSE_ROUND_MESSAGE,
    'tie': TIE_ROUND_MESSAGE
}

router = Router()
logger = get_logger(__name__)

def format_score_message(user_score: int, bot_score: int) -> str:
    return f"\n\n📊 Счёт: {user_score} : {bot_score}"

async def finish_match(message: Message, user_id: int, result: str,
                       user_score: int, bot_score: int, response: str) -> None:
    # Обновляем данные
    update_stats(user_id, result)
    reset_game_scores(user_id)
    set_game_state(user_id, False)

    # Выбираем сообщение
    final_message = MATCH_WIN_MESSAGE if result == 'win' else MATCH_LOSE_MESSAGE
    win_animation = "5046509860389126442" if result == 'win' else None
    score_info = f"\n\n📊 Финальный счёт: {user_score} : {bot_score}"

    await message.answer(
        text=f"{response}\n\n{final_message}{score_info}",
        reply_markup=get_start_keyboard(),
        message_effect_id=win_animation,
    )

@router.message(F.text.in_(GAME_OPTIONS))
async def process_game_buttons(message: Message) -> None:
    user_id = message.from_user.id
    user_info = user_log_info(message.from_user)

    if not is_game_active(user_id):
        await message.answer(NO_ACTIVE_GAME_MESSAGE, reply_markup=get_start_keyboard())
        return

    user_choice = message.text
    logger.debug(f"{user_info}: выбрал {user_choice}")

    bot_choice = choice(GAME_OPTIONS)
    logger.debug(f"{user_info}: бот выбрал {bot_choice}")

    result = determine_winner(user_choice, bot_choice)
    logger.debug(f"{user_info}: результат раунда: {result}")

    user_score, bot_score = update_game_score(user_id, result)

    round_message = ROUND_MESSAGES[result]

    score_message = format_score_message(user_score, bot_score)
    response = (
        f"{round_message}\n"
        f"Твой выбор: {user_choice}\n"
        f"Мой выбор: {bot_choice}"
        f"{score_message}"
    )

    # Проверяем, закончился ли матч
    if user_score >= TARGET_SCORE:
        logger.info(f"{user_info}: выиграл матч со счётом {user_score}:{bot_score}")
        await finish_match(message, user_id, 'win', user_score, bot_score, response)
    elif bot_score >= TARGET_SCORE:
        logger.info(f"{user_info}: проиграл матч со счётом {user_score}:{bot_score}")
        await finish_match(message, user_id, 'lose', user_score, bot_score, response)
    else:
        # Игра продолжается
        await message.answer(
            text=f"{response}\n\n{CHOOSE_OPTION_MESSAGE}",
            reply_markup=get_game_keyboard()
        )