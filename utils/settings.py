from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN")
        )
    )

Settings = get_settings('input.txt')
print(Settings)