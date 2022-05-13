import requests
from bs4 import BeautifulSoup


def scrapeCoinSite(coin):
    serverData = requests.get(f"https://coinmarketcap.com/currencies/{coin}").content
    parsedHTML = BeautifulSoup(serverData, "html.parser")

    elements = {}
    elements["priceValue"] = parsedHTML.select_one("div.priceValue")
    elements["upOrDownParent"] = parsedHTML.select_one("span.feeyND")
    if elements["upOrDownParent"] is None:
        elements["upOrDownParent"] = parsedHTML.select_one("span.gEePkg")
    elements["lowValue"] = parsedHTML.select_one("div.lipEFG")
    elements["highValue"] = parsedHTML.select_one("div.SjVBR")
    elements["statsValue"] = parsedHTML.select_one("div.statsValue")

    print(coin)
    for _, value in elements.items():
        print(value.text)
    print("\n")


coins = ["bitcoin", "ethereum", "cardano", "polygon", "chainlink", "uniswap"]
for each in coins:
    scrapeCoinSite(each)
