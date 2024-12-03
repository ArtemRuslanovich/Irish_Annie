import asyncio
from aiogram import types
from aiogram import Bot
from ai_message import handle_user_message
from utils.dbconnect import Request
from typing import Dict
from aiogram.types import Message

# Симуляция объекта Bot
class MockBot:
    async def send_message(self, chat_id, text, parse_mode=None, reply_markup=None):
        print(f"Sending message to chat {chat_id}: {text}")

# Симуляция объекта Request
class MockRequest:
    async def check_credits(self, user_id, connector):
        return True  # Предполагаем, что у пользователя достаточно кредитов

    async def subtract_credits(self, user_id, connector):
        print("Credits subtracted")

# Симуляция объекта Message
class MockMessage:
    def __init__(self, chat_id, text, from_user):
        self.chat = types.Chat(id=chat_id)
        self.text = text
        self.from_user = from_user

# Симуляция объекта User
class MockUser:
    def __init__(self, user_id):
        self.id = user_id

# Создание объектов MockBot и MockRequest
bot = MockBot()
request = MockRequest()

# Пример использования функции handle_user_message
async def test_handle_user_message():
    user_id = 12345  # Предположим, что это ID пользователя
    chat_id = 'fake_chat_id'  # Предположим, что это ID чата

    # Создаем объект MockMessage, передаем его в функцию handle_user_message
    message = MockMessage(chat_id, "Test message", MockUser(user_id))

    # Вызываем функцию handle_user_message
    await handle_user_message(message, bot, request)

# Запуск теста
asyncio.run(test_handle_user_message())