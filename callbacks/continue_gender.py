from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import gender_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def customer0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_customer)
    await callback.message.edit_text(
        f"- Select your gender" \
        f"- Gender is about how you want to be perceived during your NSFW experience",
        reply_markup=gender_keyboard
    )