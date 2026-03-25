
import requests
from bs4 import BeautifulSoup
from notifier import send_telegram_message

URL = "https://www.amazon.in/dp/B0FQFV2XKS"
TARGET_PRICE = 150000

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-IN,en;q=0.9",
}


def get_price():
    response = requests.get(URL, headers=HEADERS)
    print("STATUS:", response.status_code)

    soup = BeautifulSoup(response.text, "lxml")

    price_selectors = [
        "span.a-price span.a-offscreen",      # Most common
        "span.a-price-whole",                 # Backup
        "#priceblock_ourprice",
        "#priceblock_dealprice",
        "#priceblock_saleprice",
        "span.a-color-price",                 # Promo layout
    ]

    for selector in price_selectors:
        element = soup.select_one(selector)
        if element:
            price_text = element.get_text().strip()
            price = (
                price_text.replace("₹", "")
                .replace(",", "")
                .replace(".00", "")
            )
            if price.isdigit():
                return int(price)

    # DEBUG: save page if price not found
    with open("debug_amazon.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print("⚠️ Price selector failed. HTML saved as debug_amazon.html")
    return None



def main():
    price = get_price()

    if price is None:
        print("❌ Price not found")
        return

    print(f"💰 Current Price: ₹{price}")

    if price <= TARGET_PRICE:
        send_telegram_message(
            f"🔥 PRICE DROP ALERT!\n\n"
            f"Product price is now ₹{price}\n"
            f"{URL}"
        )
        print("✅ Alert sent to Telegram")
    else:
        print("⏳ Price is still higher than target")


if __name__ == "__main__":
    main()
