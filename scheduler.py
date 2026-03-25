import requests

BOT_TOKEN = "7869285174:AAG7tLxec_9FJKu5I0B8Pc9DvGYCyy6vXF4"
CHAT_ID = "8006409098"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

# TEST MESSAGE
if __name__ == "__main__":
    send_telegram_message("✅ Telegram integration working!")
