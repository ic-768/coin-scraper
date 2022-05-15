import requests
import threading
from bs4 import BeautifulSoup


def scrapeCoinSite(coin: str):
    serverData = requests.get(f"https://coinmarketcap.com/currencies/{coin}").content
    parsedHTML = BeautifulSoup(serverData, "html.parser")
    get = parsedHTML.select_one

    elements = {}
    elements["Price"] = get("div.priceValue")
    elements["UpOrDown"] = get("span.feeyND") or get("span.gEePkg")
    elements["Low"] = get("div.lipEFG")
    elements["High"] = get("div.SjVBR")
    elements["Stats"] = get("div.statsValue")

    print(coin, [[i, e.text] for i, e in elements.items()])


coins = ["bitcoin", "ethereum", "cardano", "polygon", "chainlink", "uniswap"]

[threading.Thread(target=scrapeCoinSite, args=(c,)).start() for c in coins]
