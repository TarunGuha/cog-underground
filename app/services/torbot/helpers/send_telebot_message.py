import requests


def send_telegram_message(payload):
    headers = {"Content-Type": "application/json"}

    endpoint = "https://api.telegram.org/bot{{telegram_bot_token}}/sendMessage"

    response = requests.post(endpoint, headers=headers, data=payload)

    return response