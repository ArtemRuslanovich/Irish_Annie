from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import profile_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm
from utils.dbconnect import Request  # Подразумевается, что у вас есть класс Request для работы с базой данных

async def profile(callback: CallbackQuery, state: FSMContext, request: Request):
    # Получаем информацию из базы данных
    user_id = callback.from_user.id
    credits, user_id = await request.get_credits_and_id(user_id)

    # Устанавливаем состояние
    await state.set_state(StatesForm.get_profile)

    # Отправляем сообщение с информацией о кредитах и ID пользователя
    message_text = f"CREDITS AVAILABLE: {credits}\n\n\n 🔎 User ID: {user_id}"
    await callback.message.edit_text(
        message_text,
        reply_markup=profile_keyboard
    )