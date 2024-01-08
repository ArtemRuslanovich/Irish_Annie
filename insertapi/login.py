import requests

# Словарь для отслеживания соответствия user_id и chat_id
user_chat_mapping = {}

def authenticate_and_create_chat(user_id):
    # Проверяем, был ли уже создан chat_id для данного пользователя
    if user_id in user_chat_mapping:
        # Если уже есть, используем сохраненный chat_id
        return user_chat_mapping[user_id]

    url_auth = "https://api.insertchatgpt.com/v1/auth/login"

    payload_auth = {'email': 'annie@irishannie.com', 'password': 'Irishannie123!'}
    headers_auth = {}

    with requests.Session() as session:
        auth_response = session.post(url_auth, headers=headers_auth, data=payload_auth)

        if auth_response.status_code == 200:
            auth_response_json = auth_response.json()
            token = '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'
            app_uid = auth_response_json.get('app', {}).get('uid')

            if app_uid:
                alt_url = "https://api.insertchatgpt.com/v1/embeds/chats"
                alt_payload = {'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593', 'label': user_id}
                headers_alt = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

                alt_response = session.post(alt_url, headers=headers_alt, json=alt_payload)
                alt_response_json = alt_response.json()

                computed_messages = alt_response_json.get('computed_messages', [])

                if computed_messages:
                    chat_uid = computed_messages[0].get('chat_uid', '')

                    # Сохраняем chat_id в словаре user_chat_mapping
                    user_chat_mapping[user_id] = chat_uid

                    return chat_uid
                else:
                    print("Error: 'chat_uid' not found in the computed_messages")
            else:
                print("Error: 'pivot_app_uid' not found in the user data")
        else:
            print("Error: Authentication request failed with status code", auth_response.status_code)