import streamlit as st
from scraper.auction_sites import scrape_storagetreasures
from scraper.resale_sites import get_ebay_prices
from scraper.social_media import scrape_reddit_sentiment
from analysis.valuation import calculate_undervalue_score


def run_dashboard():
    st.title("📦 Auction Hunter Dashboard")
    st.write("Discover undervalued storage auctions in real time.")

    auctions = scrape_storagetreasures()
    st.write(f"Found {len(auctions)} auctions")

    for auction in auctions[:5]:
        st.subheader(auction["title"])
        st.write(f"Current Price: {auction['price']}")
        st.write(f"[View Auction]({auction['link']})")

        resale_estimate = get_ebay_prices("vintage guitar")
        sentiment_score = scrape_reddit_sentiment("storage auction")
        undervalue_score = calculate_undervalue_score(
            auction['price'], resale_estimate, sentiment_score
        )

        st.metric(label="Resale Estimate", value=resale_estimate)
        st.metric(label="Sentiment Score", value=sentiment_score)
        st.metric(label="Undervalue Score", value=undervalue_score)


if __name__ == "__main__":
    run_dashboard()