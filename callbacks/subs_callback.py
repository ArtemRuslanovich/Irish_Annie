from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.subs import subs_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm

async def subs_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        f"🔥🔥🔥  Choose a monthly subscription and get up to 50% off ⭐️", reply_markup=subs_keyboard
    )