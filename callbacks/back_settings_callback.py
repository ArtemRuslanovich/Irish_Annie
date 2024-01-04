from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import settings_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def back_settings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        f"Settings",reply_markup=settings_keyboard
    )
    await state.set_state(StatesForm.get_settings)