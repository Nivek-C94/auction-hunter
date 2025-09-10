from botasaurus_driver import Driver
from bs4 import BeautifulSoup
import time


def scrape_storagetreasures():
    url = "https://www.storagetreasures.com/auctions"
    auctions = []

    with Driver(stealth=True) as driver:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for card in soup.select(".auction-card"):
            try:
                title = card.select_one(".auction-title").text.strip()
                price = card.select_one(".current-bid").text.strip()
                link = "https://www.storagetreasures.com" + card.select_one("a")["href"]
                auctions.append({"title": title, "price": price, "link": link})
            except Exception:
                continue

    return auctions