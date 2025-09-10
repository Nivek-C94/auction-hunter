from analysis.valuation import calculate_undervalue_score
from scraper.auction_sites import scrape_storagetreasures
from scraper.resale_sites import get_ebay_prices
from scraper.social_media import scrape_reddit_sentiment


def main():
    print("🚀 Auction Hunter starting...")

    auctions = scrape_storagetreasures()
    print(f"Found {len(auctions)} auctions")

    for auction in auctions[:5]:
        print("\nAuction:", auction)
        resale_estimate = get_ebay_prices("vintage guitar")
        sentiment = scrape_reddit_sentiment("storage auction")
        undervalue_score = calculate_undervalue_score(
            auction["price"], resale_estimate, sentiment)

        print(f"Estimated resale value: {resale_estimate}")
        print(f"Social sentiment score: {sentiment}")
        print(f"Undervalue score: {undervalue_score}")

        if undervalue_score > 100:  # simple threshold
            from ui.alerts import send_email_alert
            send_email_alert(
                subject="🔥 Undervalued Auction Found!",
                body=f"Auction: {auction['title']}\nPrice: {auction['price']}\nResale: {resale_estimate}\nScore: {undervalue_score}\nLink: {auction['link']}",
                to_email="you@example.com",
                from_email="bot@example.com",
                smtp_server="smtp.example.com",
                smtp_port=587,
                username="bot@example.com",
                password="yourpassword"
            )


if __name__ == "__main__":
    main()
