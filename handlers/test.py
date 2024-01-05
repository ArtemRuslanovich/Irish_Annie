import requests

url = "https://api.insertchatgpt.com/v1/embeds/messages"
payload = {'chat_uid': '87b1dfd6-424f-405e-8b0a-15619ba51fb5', 'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'user_input': 'Say Yes'}
headers = {}

response = requests.post(url, data=payload, headers=headers)
print(response.text)
