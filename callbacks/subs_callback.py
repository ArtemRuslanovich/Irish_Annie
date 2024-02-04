from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.subs import subs_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm

async def info(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_info)
    await callback.message.edit_text(
        f"🔥🔥🔥  Choose a monthly subscription and get up to 50% off ⭐️", reply_markup=subs_keyboard
    )