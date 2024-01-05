import requests

def authenticate_and_create_chat(user_id):
    url = "https://api.insertchatgpt.com/v1/auth/login"

    payload = {'email': 'annie@irishannie.com', 'password': 'Irishannie123!'}
    headers = {}

    with requests.Session() as session:
        auth_response = session.post(url, headers=headers, data=payload)

        # Check if the authentication was successful (HTTP status code 200)
        if auth_response.status_code == 200:
            auth_response_json = auth_response.json()

            token = 'MTIzNzE.3R6o6Nw0B_0HaaBZWdbTrn7HRDfzG2RyqmiNhAMPfMqnZQNt1djxODJYK8Ky'
            app_uid = auth_response_json.get('app', {}).get('uid')

            if app_uid:
                # Construct URL for the alternate request
                alt_url = "https://api.insertchatgpt.com/v1/embeds/chats"

                # Use a dictionary for the payload
                alt_payload = {
                    'widget_uid': '7acefd42-643d-4aaa-a013-8a91ff02e593',
                    'label': user_id
                }

                # Add token to headers
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                }

                # Use json parameter for the payload
                alt_response = session.post(alt_url, headers=headers, json=alt_payload)

                alt_response_json = alt_response.json()
                computed_messages = alt_response_json.get('computed_messages', [])

                # Check if there are computed messages
                if computed_messages:
                    chat_uid = computed_messages[0].get('chat_uid', '')
                    return chat_uid
                else:
                    print("Error: 'chat_uid' not found in the computed_messages")
            else:
                print("Error: 'pivot_app_uid' not found in the user data")
        else:
            print("Error: Authentication request failed with status code", auth_response.status_code)


authenticate_and_create_chat(673539334)