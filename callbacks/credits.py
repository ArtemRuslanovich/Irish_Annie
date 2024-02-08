from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.credits import get_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def credits(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_credits)
    user_id = callback.from_user.id
    keyboard = await get_keyboard(user_id)
    await callback.message.edit_text(
        f"💳 More credits, more fun with Annie. Choose now. 👄👅",
        reply_markup=keyboard
    )