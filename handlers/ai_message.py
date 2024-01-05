import requests
from aiogram import Bot, types
from aiogram.enums import ParseMode
from insertapi.login import authenticate_and_create_chat
from utils.postgresdata import close_db_connection, connect_to_db
from utils.dbconnect import Request
import json

# Handle user messages
async def handle_user_message(message: types.Message, bot: Bot, request: Request):
    user_id = message.from_user.id
    words_count = len(message.text.split())
    chat_id = authenticate_and_create_chat(user_id)

    # Check if the user has enough credits
    enough_credits = await Request.check_credits(user_id, words_count, request.connector)

    if enough_credits:
        # Process the user's message and generate a response
        url = "https://api.insertchatgpt.com/v1/embeds/messages"
        payload = {'chat_uid': chat_id, 'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'user_input': message.text}
        headers = {}

        response = requests.post(url, headers=headers, data=payload)

        try:
            response_json = response.json()
            # Check if the response contains a message
            if 'message' in response_json:
                response_text = response_json['message']
                await bot.send_message(chat_id=message.chat.id, text=response_text, parse_mode=ParseMode.MARKDOWN)
            else:
                await bot.send_message(chat_id=message.chat.id, text="Unexpected response from the API.")
        except json.decoder.JSONDecodeError:
            print("API response content:", response.content)  # Добавьте эту строку
            await bot.send_message(chat_id=message.chat.id, text="Error decoding JSON in the API response.")
    else:
        # Inform the user about insufficient credits
        await bot.send_message(chat_id=message.chat.id, text="You don't have enough credits. Please purchase more.")