from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from utils.dbconnect import Request
from utils.statesform import StatesForm



async def set_gender_male(callback: CallbackQuery, state: FSMContext, request: Request):
    user_id = callback.from_user.id
    await request.set_gender(user_id, 'male')
    await callback.message.answer('Gender set to Male')

    # Спросим имя
    await callback.message.answer("Now, what is your name?")
    await state.set_state(StatesForm.set_name)

async def set_gender_female(callback: CallbackQuery, state: FSMContext, request: Request):
    user_id = callback.from_user.id
    await request.set_gender(user_id, 'female')
    await callback.message.answer('Gender set to Female')

    # Спросим имя
    await callback.message.answer("Now, what is your name?")
    await state.set_state(StatesForm.set_name)