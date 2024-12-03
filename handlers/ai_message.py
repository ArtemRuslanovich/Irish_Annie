import json
import requests
from aiogram import types
from aiogram.enums import ParseMode
from aiogram import Bot
from insertapi.login import authenticate_and_create_chat
from utils.dbconnect import Request
from typing import Dict
from keyboards.credits import get_keyboard
from keyboards.feedback import feedback_keyboard
from aiogram.utils import markdown
import re

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram import types

# Словарь для отслеживания соответствия user_id и chat_id
user_chat_mapping: Dict[int, str] = {}

async def handle_user_message(message: Message, bot: Bot, request: Request):
    user_id = message.from_user.id

    # Вызов синхронной функции для аутентификации и создания chat_id
    chat_id = authenticate_and_create_chat(user_id)

    # Вызов асинхронной функции для получения клавиатуры
    keyboard = await get_keyboard(user_id)

    # Получаем данные о кредитах. Преобразуем этот вызов в синхронный, если нужно
    enough_credits = request.check_credits(user_id, request.connector)  # Это синхронная функция

    if enough_credits:
        # Подготовка запроса к API с синхронной отправкой данных
        url = "https://api.insertchatgpt.com/v1/embeds/messages"
        payload = {'chat_uid': chat_id, 'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'input': message.text, 'disable_stream': 'false', 'role': 'user', 'dynamic_context': '', 'dynamic_questions': '', 'dynamic_system_behavior': ''}
        headers = {}

        # Синхронный запрос
        response = requests.post(url, headers=headers, data=payload)

        try:
            # Декодируем ответ и обрабатываем его
            response_text = response.content.decode("utf-8")
            print(response_text)
            response_text = response_text.split('[MESSAGE_UID]')[0].strip()
            response_text = response_text.replace("*", "_", 1).replace("*", "_", -1).replace("_", ")", 1).replace("_", "(", 1)

            # Теперь нужно вызвать синхронную функцию для вычитания кредита
            request.subtract_credits(user_id, request.connector)  # Синхронная операция

            # Отправляем ответ пользователю
            await bot.send_message(chat_id=message.chat.id, text=response_text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

        except Exception as e:
            print("Error processing API response:", e)
            await bot.send_message(chat_id=message.chat.id, text="Error processing API response.")
    else:
        # Сообщаем пользователю об отсутствии кредитов
        await bot.send_message(chat_id=message.chat.id, text="You don't have enough credits. Please purchase more.", reply_markup=keyboard)


def process_message_text(text):
    # Проверяем, начинается ли текст с I{ и заканчивается ли на }
    if text.startswith("I ") and text.endswith("."):
        # Извлекаем текст между I{ и }
        inner_text = text[2:-1]

        # Применяем курсив к внутреннему тексту
        italic_text = markdown.markdown(inner_text, extensions=['italic'])

        # Возвращаем новый текст с курсивом
        return italic_text
    else:
        # Возвращаем оригинальный текст
        return text

# Обработчик для оценки ответа
async def process_feedback(callback_query: types.CallbackQuery, bot: Bot):
    user_id = callback_query.from_user.id

    if callback_query.data == "like":
        # Отправляем благодарность за положительный фидбек
        await callback_query.answer(text="Thank you for your positive feedback! 😊", show_alert=True)
        await bot.send_message(text='💋', chat_id=callback_query.message.chat.id)
    elif callback_query.data == "dislike":
        # Отправляем уведомление о том, что сообщение передано разработчику для проверки
        await callback_query.answer(text="Your feedback has been forwarded to the developer for review. Thank you for your input! 🙏", show_alert=True)



        