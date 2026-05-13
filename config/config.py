from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class ProxySettings:
    type: str
    ip: str
    port: str
    login: str
    password: str

    @property
    def url(self) -> str:
        """Возвращает готовый URL прокси для использования в aiogram"""
        auth = ""
        if self.login and self.password:
            auth = f"{self.login}:{self.password}@"
        return f"{self.type}://{auth}{self.ip}:{self.port}"

@dataclass
class Config:
    bot: TgBot
    log: LogSettings
    proxy: ProxySettings

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(token=env('BOT_TOKEN')),
        log=LogSettings(level=env('LOG_LEVEL'), format=env('LOG_FORMAT')),
        proxy=ProxySettings(
            type=env('PROXY_TYPE', default='http'),
            ip=env('PROXY_IP'),
            port=env('PROXY_PORT'),
            login=env('PROXY_LOGIN'),
            password=env('PROXY_PASSWORD')
        )
    )