import requests
from aiogram import types
from aiogram.enums import ParseMode
from aiogram import Bot
from insertapi.login import authenticate_and_create_chat
from utils.dbconnect import Request
from typing import Dict
from keyboards.credits import credits_keyboard
from keyboards.feedback import feedback_keyboard



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# Словарь для отслеживания соответствия user_id и chat_id
user_chat_mapping: Dict[int, str] = {}

async def handle_user_message(message: types.Message, bot: Bot, request: Request):
    user_id = message.from_user.id
    words_count = len(message.text.split())
    
    # Создаем или получаем chat_id
    chat_id = authenticate_and_create_chat(user_id)

    # Проверяем, есть ли у пользователя достаточно кредитов
    enough_credits = await Request.check_credits(user_id, words_count, request.connector)

    if enough_credits:
        # Обрабатываем сообщение пользователя и генерируем ответ
        url = "https://api.insertchatgpt.com/v1/embeds/messages"
        payload = {'chat_uid': chat_id, 'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'user_input': message.text}
        headers = {}

        response = requests.post(url, headers=headers, data=payload)

        try:
            response_text = response.content.decode("utf-8")
            # Проверяем, содержит ли ответ сообщение
            if 'MESSAGE_UID' in response_text:
                # Извлекаем часть сообщения до MESSAGE_UID
                response_text = response_text.split('[MESSAGE_UID]')[0].strip()

                # Отнимаем кредиты из базы данных
                await Request.subtract_credits(user_id, words_count, request.connector)

                # Отправляем ответ с инлайн-клавиатурой
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=response_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=feedback_keyboard
                )
            else:
                await bot.send_message(chat_id=message.chat.id, text="Unexpected response from the API.")
        except Exception as e:
            print("Error processing API response:", e)
            await bot.send_message(chat_id=message.chat.id, text="Error processing API response.")
    else:
        # Информируем пользователя о недостаточном количестве кредитов
        await bot.send_message(chat_id=message.chat.id, text="You don't have enough credits. Please purchase more.", reply_markup=credits_keyboard)


# Обработчик для оценки ответа
async def process_feedback(callback_query: types.CallbackQuery, bot: Bot):
    user_id = callback_query.from_user.id

    if callback_query.data == "like":
        # Отправляем благодарность за положительный фидбек
        await callback_query.answer(text="Thank you for your positive feedback! 😊", show_alert=True)
    elif callback_query.data == "dislike":
        # Отправляем уведомление о том, что сообщение передано разработчику для проверки
        await callback_query.answer(text="Your feedback has been forwarded to the developer for review. Thank you for your input! 🙏", show_alert=True)


        