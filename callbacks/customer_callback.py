from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import customer_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def customer(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_customer)
    await callback.message.edit_text(
        f"- Choose how Annie calls you" \
        f"- Gender is about how you want to be perceived during your NSFW experience",
        reply_markup=customer_keyboard
    )