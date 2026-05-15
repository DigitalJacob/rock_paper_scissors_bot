![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

# Rock Paper Scissors Bot

A feature-rich Telegram bot for playing the classic Rock Paper Scissors game with best of 3 rounds, score tracking, and elegant keyboard interface.

## Tech Stack

- **Language:** Python 3.12+
- **Framework:** aiogram 3.x
- **HTTP Client:** aiohttp with proxy support (aiohttp-socks)
- **Configuration:** python-dotenv / environs
- **Logging:** Built-in logging module with file rotation

## Features

- ✊ Classic gameplay — Rock beats Scissors, Scissors beats Paper, Paper beats Rock
- 🏆 Best of 3 rounds — first to win 3 rounds wins the match
- 📊 Statistics tracking — wins, losses, and win rate
- 🎨 User-friendly interface — interactive buttons with emojis
- 🔌 Proxy support — works with HTTP/HTTPS/SOCKS5 proxies
- 📝 Comprehensive logging — debug and monitor bot activity

## Commands

| Command | Description |
|---------|-------------|
| /start | Start the bot and see welcome message |
| /help | Display game rules and instructions |
| /stat | View your personal statistics |
| /cancel | Cancel current game session |

## Installation

1. Clone the repository:
```bash
git clone git@github.com:akovveretin/rock-paper-scissors-bot.git
cd rock-paper-scissors-bot
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```

Then edit .env and replace the example values with your own:

BOT_TOKEN — get it from @BotFather

PROXY_TYPE, PROXY_IP, PROXY_PORT, PROXY_LOGIN, PROXY_PASSWORD — add your proxy data

LOG_LEVEL — DEBUG for development, INFO for production

5. Run the bot:
```bash
python main.py
```

## Project Structure

| Path | Description |
|------|-------------|
| `config/` | Configuration management |
| `handlers/` | Message handlers |
| `keyboards/` | Reply keyboards |
| `lexicon/` | Text messages |
| `logger/` | Logging setup |
| `services/` | Business logic |
| `storage/` | User data storage |
| `main.py` | Entry point |
| `requirements.txt` | Dependencies |

## Licence

MIT License — free to use, modify, and distribute.
