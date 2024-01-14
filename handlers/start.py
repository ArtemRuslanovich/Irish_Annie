from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from utils.dbconnect import Request
from keyboards.inline import start_keyboard, continue_name_keyboard, gender_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import StatesForm


async def command_start_handler(message: Message, state: FSMContext, bot: Bot, request: Request):
    await state.set_state(StatesForm.get_start)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(text=(f"""👄 Hey there, I’m Irish Annie. Talk to me and I’ll warm your heart (among other things) 😘

Let's start with a quick question...are you male or female?"""),chat_id=message.from_user.id, reply_markup=gender_keyboard)

async def command_help_handler(message: Message) -> None:
    await message.reply(f"""❓ **How to Use Annie: Quick Guide**

1. 🚀 **Start:** Begin your adventure with Annie by typing /start.
2. 🎭 **Commands:** Use /help to explore available commands.
3. 💬 **Chat:** Engage in conversations with Annie. She loves to chat!
4. ℹ️ **Info:** Learn more about Annie and her features with /info.
5. ⚙️ **Settings:** Personalize your experience using /settings.


📚 **Explore, Chat, and Enjoy the Annie experience!**""")

async def command_menu_handler(message: Message, state: FSMContext, bot: Bot, request: Request):
    await state.set_state(StatesForm.get_start)
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(text=(f"""💋 Hey there, adventurous soul! Welcome to our vibrant universe! 🥰

I'm Annie, your personal guide to extraordinary experiences. 🌟 Ready to dive into a world of wonders? Let's make every interaction magical! 💫

Feel free to explore, ask questions, or embark on a delightful journey with me. 🌺"""),chat_id=message.from_user.id, reply_markup=start_keyboard)