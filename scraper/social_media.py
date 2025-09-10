from botasaurus_driver import Driver
from bs4 import BeautifulSoup
import time
from textblob import TextBlob


def scrape_reddit_sentiment(keyword="storage auction"):
    """
    Scrape Reddit search results for a keyword and compute sentiment.
    """
    url = f"https://www.reddit.com/search/?q={keyword.replace(' ', '%20')}"
    sentiments = []

    with Driver(stealth=True, user_agent="desktop") as driver:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        posts = soup.select("h3")
        for post in posts[:10]:
            text = post.text
            polarity = TextBlob(text).sentiment.polarity
            sentiments.append(polarity)

    return sum(sentiments)/len(sentiments) if sentiments else 0