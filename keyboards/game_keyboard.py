from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_game_keyboard() -> ReplyKeyboardMarkup:
    """Возвращает игровую клавиатуру с кнопками 🪨 ✂️ 📄"""
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='🪨'),
            KeyboardButton(text='✂️'),
            KeyboardButton(text='📄')
        ]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )