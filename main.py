from scraper.auction_sites import scrape_storagetreasures
from scraper.resale_sites import get_ebay_prices
from scraper.social_media import scrape_reddit_sentiment


def main():
    print("🚀 Auction Hunter starting...")

    auctions = scrape_storagetreasures()
    print(f"Found {len(auctions)} auctions")

    for auction in auctions[:3]:
        print("\nAuction:", auction)
        value_estimate = get_ebay_prices("vintage guitar")
        sentiment = scrape_reddit_sentiment("storage auction")
        print(f"Estimated resale value: {value_estimate}")
        print(f"Social sentiment score: {sentiment}")


if __name__ == "__main__":
    main()