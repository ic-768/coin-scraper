import requests
from bs4 import BeautifulSoup

# GET server data
bitcoin = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
ethereum = requests.get("https://coinmarketcap.com/currencies/ethereum/")
cardano = requests.get("https://coinmarketcap.com/currencies/cardano/")
polygon = requests.get("https://coinmarketcap.com/currencies/polygon/")
chainlink = requests.get("https://coinmarketcap.com/currencies/chainlink/")
uniswap = requests.get("https://coinmarketcap.com/currencies/uniswap/")
cacheGold = requests.get("https://coinmarketcap.com/currencies/cache-gold")

# Parse HTML
bitSoup = BeautifulSoup(bitcoin.content, "html.parser")
ethSoup = BeautifulSoup(ethereum.content, "html.parser")
adaSoup = BeautifulSoup(cardano.content, "html.parser")
polygon = BeautifulSoup(polygon.content, "html.parser")
chainlink = BeautifulSoup(chainlink.content, "html.parser")
uniswap = BeautifulSoup(uniswap.content, "html.parser")
cacheGold = BeautifulSoup(cacheGold.content, "html.parser")

bitSoup.name = "BITSOUP"
ethSoup.name = "ETHSOUP"
adaSoup.name = "ADASOUP"
polygon.name = "POLYGON"
chainlink.name = "CHAINLINK"
uniswap.name = "UNISWAP"
cacheGold.name = "CACHEGOLD"

for each in [bitSoup, ethSoup, adaSoup, polygon, chainlink, uniswap, cacheGold]:
    print(each.name, "\n")
    priceValue = each.find("div", class_="priceValue").text
    upOrDownParent = each.find("span", class_="feeyND")
    if not hasattr(upOrDownParent, "text"):
        upOrDownParent = each.find("span", class_="gEePkg").text
    else:
        upOrDownParent = upOrDownParent.text
    lowValue = each.find("div", class_="lipEFG").text
    highValue = each.find("div", class_="SjVBR").text
    statsValue = each.find("div", class_="statsValue").text

    print(priceValue)
    print(upOrDownParent)
    print(lowValue)
    print(highValue)
    print(statsValue)
    print("\n")
