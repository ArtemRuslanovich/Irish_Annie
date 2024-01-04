from aiogram.types import CallbackQuery
from aiogram import Router, F, Bot, Dispatcher
from keyboards.inline import info_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm

async def info(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StatesForm.get_info)
    await callback.message.edit_text(
        f"""🌈 Alisa is not just a bot; she's a gateway to limitless possibilities! Dive into a magical experience with Alisa's enchanting features.

🔮 **Features:**
- 🤖 **Smart Conversations:** Alisa loves a good chat! Engage in meaningful conversations and let her surprise you.
- 🌐 **Global Insights:** Connect with users worldwide and discover diverse perspectives.
- 🎉 **Fun Interactions:** From games to jokes, Alisa knows how to keep the fun alive!

📚 **How to Use:**
1. 🚀 **Start:** Hit /start to embark on your magical journey.
2. ❓ **Help:** Need assistance? Simply type /help for quick guidance.

🌟 **Let the magic begin!""",
        reply_markup=info_keyboard
    )