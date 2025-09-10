def calculate_undervalue_score(auction_price, resale_estimate, sentiment_score):
    """
    Compute a simple undervalue score combining:
    - Auction price
    - Resale estimate (from eBay/Craigslist)
    - Sentiment score (from Reddit/Twitter)

    Returns a float where higher = more undervalued.
    """
    try:
        if resale_estimate is None:
            return 0
        margin = resale_estimate - float(auction_price.replace("$", "").replace(",", ""))
        score = margin * (1 + sentiment_score)
        return round(score, 2)
    except Exception:
        return 0