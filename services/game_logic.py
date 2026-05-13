from lexicon.lexicon_ru import WIN_ROUND_MESSAGE, LOSE_ROUND_MESSAGE, TIE_ROUND_MESSAGE


def determine_winner(user_choice: str, bot_choice: str) -> str:
    if user_choice == bot_choice:
        return 'tie'

    win_conditions = {
        '🪨': '✂️',
        '✂️': '📄',
        '📄': '🪨'
    }

    return 'win' if win_conditions[user_choice] == bot_choice else 'lose'


def format_game_result(user_choice: str, bot_choice: str, result: str) -> str:
    """Форматирует сообщение с результатом"""
    result_messages = {
        'win': WIN_ROUND_MESSAGE,
        'lose': LOSE_ROUND_MESSAGE,
        'tie': TIE_ROUND_MESSAGE,
    }

    return (
        f"Твой выбор: {user_choice}\n"
        f"Мой выбор: {bot_choice}\n\n"
        f"{result_messages[result]}"
    )


