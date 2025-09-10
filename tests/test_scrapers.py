import pytest
from scraper.auction_sites import scrape_storagetreasures


def test_scrape_storagetreasures_returns_list():
    auctions = scrape_storagetreasures()
    assert isinstance(auctions, list)
    if auctions:
        assert "title" in auctions[0]
        assert "price" in auctions[0]
        assert "link" in auctions[0]