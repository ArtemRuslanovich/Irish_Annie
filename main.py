import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
import schedule
from callbacks.back_start_callback import back_start
from callbacks.back_settings_callback import back_settings
from callbacks.bot_settings_callback import bot_settings
from callbacks.customer_callback import customer
from callbacks.info_callback import info
from callbacks.profile_callback import profile
from callbacks.settings_callback import settings
from handlers.start import command_start_handler, command_help_handler
from utils.settings import Settings
from aiogram import F
from aiogram.filters import Command
from Commands.commands import set_commands
from middlewares.dbmiddleware import Dbsession
from utils.postgresdata import create_pool
from callbacks.credits import credits

dp = Dispatcher()
router = Router()


async def start_bot(bot: Bot):
    await set_commands(bot)
    pool_connect = await create_pool()
    dp.message.register(command_start_handler, Command(commands=['start']))
    dp.message.register(command_help_handler, Command(commands=['help']))
    dp.callback_query.register(settings, F.data.startswith('settings'))
    dp.callback_query.register(profile, F.data.startswith('profile'))
    dp.callback_query.register(info, F.data.startswith('info'))
    dp.callback_query.register(back_start, F.data.startswith('back_start'))
    dp.callback_query.register(back_settings, F.data.startswith('back_settings'))
    dp.callback_query.register(customer, F.data.startswith('customer'))
    dp.callback_query.register(bot_settings, F.data.startswith('bot_settings'))
    dp.callback_query.register(credits, F.data.startswith('show_credits'))


    dp.update.middleware.register(Dbsession(pool_connect))

dp.startup.register(start_bot)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(Settings.bots.bot_token, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

    while True:
        await dp.loop.run_until_complete(schedule.run_pending())
        await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())