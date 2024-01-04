from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import start_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def back_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        f"""💋 Hey there, adventurous soul! Welcome to our vibrant universe! 🥰

I'm Alisa, your personal guide to extraordinary experiences. 🌟 Ready to dive into a world of wonders? Let's make every interaction magical! 💫

Feel free to explore, ask questions, or embark on a delightful journey with me. 🌺""", reply_markup=start_keyboard
    )
    await state.set_state(StatesForm.get_start),