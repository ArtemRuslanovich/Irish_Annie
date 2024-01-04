from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import types

from utils.dbconnect import Request
from utils.statesform import StatesForm

async def ask_for_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Please, enter your desired username:")
    await state.set_state(StatesForm.set_name)


async def process_name_input(message: types.Message, state: FSMContext, request: Request):
    user_name = message.text.strip()

    user_id = message.from_user.id
    await request.add_name(user_id, user_name)

    await state.clear()
    await message.answer(f"Your username '{user_name}' has been successfully saved!")