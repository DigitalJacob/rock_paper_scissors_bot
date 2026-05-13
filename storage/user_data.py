from dataclasses import dataclass, field
from typing import Dict

@dataclass
class CurrentGame:
    """Текущее состояние игры"""
    game_state: bool = False
    user_score: int = 0      
    bot_score: int = 0       

@dataclass
class UserStats:
    """Общая статистика пользователя"""
    total_games: int = 0
    wins: int = 0
    losses: int = 0

@dataclass
class UserData:
    current: CurrentGame = field(default_factory=CurrentGame)
    stats: UserStats = field(default_factory=UserStats)

user_games: Dict[int, UserData] = {}

def get_user_data(user_id: int) -> UserData:
    if user_id not in user_games:
        user_games[user_id] = UserData()
    return user_games[user_id]

def is_game_active(user_id: int) -> bool:
    return get_user_data(user_id).current.game_state

def set_game_state(user_id: int, state: bool) -> None:
    get_user_data(user_id).current.game_state = state

def reset_game_scores(user_id: int) -> None:
    """Сбрасывает счёт текущей игры"""
    game = get_user_data(user_id).current
    game.user_score = 0
    game.bot_score = 0

def update_game_score(user_id: int, result: str) -> tuple[int, int]:
    """
    Обновляет счёт текущей игры
    Returns: (user_score, bot_score)
    """
    game = get_user_data(user_id).current
    if result == 'win':
        game.user_score += 1
    elif result == 'lose':
        game.bot_score += 1
    return game.user_score, game.bot_score

def get_current_scores(user_id: int) -> tuple[int, int]:
    """Возвращает текущий счёт (user, bot)"""
    game = get_user_data(user_id).current
    return game.user_score, game.bot_score

def update_stats(user_id: int, result: str) -> None:
    """Обновляет общую статистику (только при завершении матча)"""
    stats = get_user_data(user_id).stats
    stats.total_games += 1
    if result == 'win':
        stats.wins += 1
    elif result == 'lose':
        stats.losses += 1
