from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import info_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm

async def info(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_info)
    await callback.message.edit_text(
        f"*"
    )