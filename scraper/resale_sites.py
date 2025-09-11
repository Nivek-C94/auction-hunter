from botasaurus_driver import Driver
from bs4 import BeautifulSoup


def get_ebay_prices(query="vintage guitar"):
    """
    Scrape eBay sold listings for average price of given query.
    Uses Botasaurus Driver.
    """
    url = (
        "https://www.ebay.com/sch/i.html?_nkw="
        f"{query.replace(' ', '+')}"
        "&LH_Sold=1&LH_Complete=1"
    )
    prices = []

    with Driver() as driver:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for item in soup.select(".s-item"):
            price_tag = item.select_one(".s-item__price")
            if not price_tag:
                continue
            try:
                value = price_tag.text.replace(
                    "$", "").replace(",", "").strip()
                price = float(value)
                prices.append(price)
            except ValueError:
                continue

    return sum(prices) / len(prices) if prices else None
