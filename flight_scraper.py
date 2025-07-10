import requests
from bs4 import BeautifulSoup

def get_flight_price(dep, arr, date):
    url = f"https://flights.qunar.com/site/oneway_list.htm?fromCity={dep}&toCity={arr}&fromDate={date}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []
    for span in soup.find_all("span", class_="price"):
        try:
            price = int(span.get_text())
            prices.append(price)
        except:
            continue

    return min(prices) if prices else None
