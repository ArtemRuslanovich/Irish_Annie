from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from utils.dbconnect import Request
from keyboards.inline import start_keyboard, continue_name_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def command_start_handler(message: Message, state: FSMContext, bot: Bot, request: Request):
    await state.set_state(StatesForm.get_start)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(text=(f"""🌈 Alisa is not just a bot; she's a gateway to limitless possibilities! Dive into a magical experience with Alisa's enchanting features.

🔮 **Features:**
- 🤖 **Smart Conversations:** Alisa loves a good chat! Engage in meaningful conversations and let her surprise you.
- 🌐 **Global Insights:** Connect with users worldwide and discover diverse perspectives.
- 🎉 **Fun Interactions:** From games to jokes, Alisa knows how to keep the fun alive!

📚 **How to Use:**
1. 🚀 **Start:** Hit /start to embark on your magical journey.
2. ❓ **Help:** Need assistance? Simply type /help for quick guidance.

🌟 **Let the magic begin!"""),chat_id=message.from_user.id, reply_markup=continue_name_keyboard)

async def command_help_handler(message: Message) -> None:
    await message.reply(f"""❓ **How to Use Alisa: Quick Guide**

1. 🚀 **Start:** Begin your adventure with Alisa by typing /start.
2. 🎭 **Commands:** Use /help to explore available commands.
3. 💬 **Chat:** Engage in conversations with Alisa. She loves to chat!
4. ℹ️ **Info:** Learn more about Alisa and her features with /info.
5. ⚙️ **Settings:** Personalize your experience using /settings.


📚 **Explore, Chat, and Enjoy the Alisa experience!**""")

async def command_menu_handler(message: Message, state: FSMContext, bot: Bot, request: Request):
    await state.set_state(StatesForm.get_start)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(text=(f"""💋 Hey there, adventurous soul! Welcome to our vibrant universe! 🥰

I'm Alisa, your personal guide to extraordinary experiences. 🌟 Ready to dive into a world of wonders? Let's make every interaction magical! 💫

Feel free to explore, ask questions, or embark on a delightful journey with me. 🌺"""),chat_id=message.from_user.id, reply_markup=start_keyboard)