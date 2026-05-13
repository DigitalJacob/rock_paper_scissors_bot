from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import AGREE_BUTTON_TEXT, DISAGREE_BUTTON_TEXT, STAT_BUTTON_TEXT


def get_start_keyboard() -> ReplyKeyboardMarkup:
    agree_button = KeyboardButton(text=AGREE_BUTTON_TEXT)
    disagree_button = KeyboardButton(text=DISAGREE_BUTTON_TEXT)
    stat_button = KeyboardButton(text=STAT_BUTTON_TEXT)

    return ReplyKeyboardMarkup(
        keyboard=[[agree_button, disagree_button], [stat_button]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )