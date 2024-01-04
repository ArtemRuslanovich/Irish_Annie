from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from utils.dbconnect import Request
from keyboards.inline import start_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def command_start_handler(message: Message, state: FSMContext, bot: Bot, request: Request):
    await state.set_state(StatesForm.get_start)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(text=f"Start",chat_id=message.from_user.id, reply_markup=start_keyboard)

async def command_help_handler(message: Message) -> None:
    await message.reply(f"Help")

