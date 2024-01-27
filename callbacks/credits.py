from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.credits import credits_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def credits(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_credits)
    await callback.message.edit_text(
        f"💳 More credits, more fun with Annie. Choose now. 👄👅",
        reply_markup=credits_keyboard
    )