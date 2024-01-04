from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import start_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def back_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        f"Start", reply_markup=start_keyboard
    )
    await state.set_state(StatesForm.get_start),