from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import profile_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm

async def profile(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_profile)
    await callback.message.edit_text(
        f"CREDITS AVAILABLE:",
        reply_markup=profile_keyboard
    )