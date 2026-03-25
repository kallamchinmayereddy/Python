import requests

BOT_TOKEN = "your_token"
CHAT_ID = "your_id"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": your_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()
