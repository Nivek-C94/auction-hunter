from botasaurus import browser, create_stealth_driver
from bs4 import BeautifulSoup


@browser(create_driver=create_stealth_driver(start_url="https://www.storagetreasures.com/auctions"))
def scrape_storagetreasures(driver, data):
    """
    Scrape auctions from StorageTreasures using a stealth driver.
    """
    soup = BeautifulSoup(driver.page_source, "html.parser")

    auctions = []
    for card in soup.select(".auction-card"):
        try:
            title = card.select_one(".auction-title").text.strip()
            price = card.select_one(".current-bid").text.strip()
            link = "https://www.storagetreasures.com" + \
                card.select_one("a")["href"]
            auctions.append({"title": title, "price": price, "link": link})
        except Exception:
            continue

    return auctions

    return auctions
