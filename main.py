import requests
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

    print(coin)
    for _, value in elements.items():
        print(value.text)
    print("\n")


coins = ["bitcoin", "ethereum", "cardano", "polygon", "chainlink", "uniswap"]

for each in coins:
    scrapeCoinSite(each)
