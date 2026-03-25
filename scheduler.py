import requests

BOT_TOKEN = "Your_token"
CHAT_ID = "Yourid"

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
