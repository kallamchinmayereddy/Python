
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/dp/B0FQFV2XKS"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price = None

# Modern Amazon price selector
price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")

if price_whole:
    price = price_whole.get_text(strip=True)
    if price_fraction:
        price += "." + price_fraction.get_text(strip=True)

print("STATUS:", response.status_code)
print("FINAL URL:", response.url)

if price:
    print("PRICE FOUND: ₹", price)
else:
    print("PRICE NOT FOUND")
