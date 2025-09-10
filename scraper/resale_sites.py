from botasaurus_driver import Driver
from bs4 import BeautifulSoup
import time


def get_ebay_prices(query="vintage guitar"):
    """
    Scrape eBay sold listings for average price of given query.
    Uses Botasaurus to simulate browser and bypass detection.
    """
    url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}&LH_Sold=1&LH_Complete=1"
    prices = []

    with Driver(stealth=True) as driver:
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for item in soup.select(".s-item"):
            price_tag = item.select_one(".s-item__price")
            if price_tag:
                try:
                    price = float(price_tag.text.replace("$", "").replace(",", "").strip())
                    prices.append(price)
                except Exception:
                    continue

    return sum(prices)/len(prices) if prices else None