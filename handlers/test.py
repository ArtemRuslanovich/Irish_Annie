import requests
import json

url = "https://api.insertchatgpt.com/v1/embeds/messages"
payload = {'chat_uid': '87b1dfd6-424f-405e-8b0a-15619ba51fb5', 'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'input': 'Say Yes', 'disable_stream': 'false', 'role': 'user', 'dynamic_context': '','dynamic_questions': '','dynamic_system_behavior': ''}
headers = {}

response = requests.post(url, data=payload, headers=headers)
response_data = json.loads(response.text)

# Извлекаем текст ответа
output_text = response_data['_readableState']['buffer']['head']['data']

# Убираем лишние символы и оставляем только текст ответа
cleaned_text = output_text.strip().split('[AI]')[1].split(']')[0]

# Выводим текст ответа
print(response_data)

