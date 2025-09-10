from textblob import TextBlob


def analyze_text_sentiment(text: str) -> float:
    """
    Perform sentiment analysis on a given text string.
    Returns polarity between -1 (negative) and 1 (positive).
    """
    try:
        return TextBlob(text).sentiment.polarity
    except Exception:
        return 0.0