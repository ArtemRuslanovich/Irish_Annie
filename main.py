import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode, ContentType
import schedule
from aiohttp import web
from callbacks.back_start_callback import back_start
from callbacks.back_settings_callback import back_settings
from callbacks.bot_settings_callback import bot_settings
from callbacks.continue_gender import customer0
from callbacks.continue_name import ask_for_name0, process_name_input0
from callbacks.customer_callback import customer
from callbacks.info_callback import info
from callbacks.profile_callback import profile
from callbacks.referal_callback import referal_system
from callbacks.set_gender import set_gender_female, set_gender_male
from callbacks.settings_callback import settings
from callbacks.subs_callback import subs_callback
from callbacks.subs_pay_callbacks.basic import process_subscribe_basic
from callbacks.subs_pay_callbacks.platinum import process_subscribe_platinum
from callbacks.subs_pay_callbacks.pro import process_subscribe_pro
from callbacks.user_name_callback import ask_for_name, process_name_input
from handlers.ai_message import handle_user_message, process_feedback
from handlers.start import command_menu_handler, command_start_handler, command_help_handler
from utils.settings import Settings
from aiogram import F
from aiogram.filters import Command
from Commands.commands import set_commands
from middlewares.dbmiddleware import Dbsession
from utils.postgresdata import create_pool
from callbacks.credits import credits
from callbacks.credits_pay.one import pre_checkout_query, send_invoice, successful_payment
from utils.statesform import StatesForm



dp = Dispatcher()
router = Router()


async def start_bot(bot: Bot):
    await set_commands(bot)
    pool_connect = await create_pool()
    dp.message.register(command_start_handler, Command(commands=['start']))
    dp.message.register(command_help_handler, Command(commands=['help']))
    dp.message.register(command_menu_handler, Command(commands=['menu']))


    dp.callback_query.register(settings, F.data.startswith('settings'))
    dp.callback_query.register(profile, F.data.startswith('profile'))
    dp.callback_query.register(referal_system, F.data.startswith('referal'))
    dp.callback_query.register(info, F.data.startswith('info'))
    dp.callback_query.register(back_start, F.data.startswith('back_start'))
    dp.callback_query.register(back_settings, F.data.startswith('back_settings'))
    dp.callback_query.register(customer, F.data.startswith('customer'))
    dp.callback_query.register(bot_settings, F.data.startswith('bot_settings'))
    dp.callback_query.register(credits, F.data.startswith('show_credits'))

    dp.callback_query.register(customer0, F.data.startswith('continue_gender'))


    dp.callback_query.register(ask_for_name0, F.data.startswith('continue_name'))
    dp.message.register(process_name_input0, StatesForm.set_name1)
    dp.callback_query.register(set_gender_male, F.data.startswith('set_male'))
    dp.callback_query.register(set_gender_female, F.data.startswith('set_female'))
    dp.callback_query.register(ask_for_name, F.data.startswith('set_name'))
    dp.message.register(process_name_input, StatesForm.set_name)
    dp.callback_query.register(set_gender_female, F.data.startswith('set_female'))

    dp.message.register(handle_user_message, F.text)

    dp.pre_checkout_query.register(pre_checkout_query)
    dp.callback_query.register(process_feedback, lambda c: c.data in ["like", "dislike"])
    dp.callback_query.register(send_invoice, F.data.startswith('credits'))
    dp.callback_query.register(subs_callback, F.data.startswith('subs'))

    dp.callback_query.register(process_subscribe_basic, F.data.startswith('subscripe_2000'))
    dp.callback_query.register(process_subscribe_pro, F.data.startswith('subscripe_5000'))
    dp.callback_query.register(process_subscribe_platinum, F.data.startswith('subscripe_10000'))

    dp.message.register(successful_payment, F.content_type==ContentType.SUCCESSFUL_PAYMENT)
    dp.update.middleware.register(Dbsession(pool_connect))

dp.startup.register(start_bot)

async def main() -> None:
    # Инициализация бота с настройками
    bot = Bot(Settings.bots.bot_token, parse_mode=ParseMode.HTML)

    # Инициализация и запуск вашего бота
    await start_bot(bot)

    # Создание aiohttp веб-приложения для Heroku
    app = web.Application()
    app.router.add_get('/', lambda request: web.Response(text="Hello, your bot is running"))
    app.router.add_post('/', lambda request: web.Response())

    # Запуск aiohttp веб-сервера
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    await site.start()

    # Запуск цикла опроса
    await dp.start_polling(bot)

    while True:
        # Запуск запланированных задач
        await dp.loop.run_until_complete(schedule.run_pending())
        await asyncio.sleep(1)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())