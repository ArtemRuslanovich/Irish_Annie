from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from utils.dbconnect import Request


async def set_gender_male(callback: CallbackQuery, state: FSMContext, request: Request):
    user_id = callback.from_user.id
    await request.set_gender(user_id, 'male')
    await callback.answer('Gender set to Male')
    await state.clear()

async def set_gender_female(callback: CallbackQuery, state: FSMContext, request: Request):
    user_id = callback.from_user.id
    await request.set_gender(user_id, 'female')
    await callback.answer('Gender set to Female')
    await state.clear()


