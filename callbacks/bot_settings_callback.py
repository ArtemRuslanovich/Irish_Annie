from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import bot_settings_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def bot_settings(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_bot_settings)
    await callback.message.edit_text(
        f"bot settings info",
        reply_markup=bot_settings_keyboard
    )