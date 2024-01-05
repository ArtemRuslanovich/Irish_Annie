from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/help", description="Help"),
        BotCommand(command="/menu", description="Menu"),
    ]
    scope_default = BotCommandScopeDefault()

    await bot.set_my_commands(commands, scope_default)