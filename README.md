# Auction Hunter

**Auction Hunter** is a hyper-adaptive system for discovering undervalued storage unit auctions. It uses [`botasaurus_driver`](https://github.com/omkarcloud/botasaurus-driver) for stealth scraping, valuation, and real-time alerts.

## 🚀 Features
- **Auction Scraper** → Crawls StorageTreasures, Lockerfox, StorageAuctions, and more.
- **Valuation Engine** → Scrapes eBay / Craigslist / Facebook Marketplace for resale value.
- **Sentiment Monitor** → Tracks Reddit/Twitter chatter for auction buzz.
- **Computer Vision** → Detects valuables in auction photos.
- **Event Awareness** → Scrapes local event calendars to predict low competition windows.
- **Fraud Detection** → Flags staged or manipulated listings.
- **UI Dashboard** → Live auction scoring and notifications.

## 📂 Project Structure
```
auction_hunter/
│── main.py                  # Orchestrator
│── scraper/
│    ├── auction_sites.py     # Auction platforms
│    ├── resale_sites.py      # Resale platforms (eBay, Craigslist)
│    ├── social_media.py      # Reddit/Twitter sentiment
│    ├── events.py            # Event scraping
│    └── housing.py           # Housing/eviction signals
│── analysis/
│    ├── vision.py            # Computer vision
│    ├── sentiment.py         # NLP analysis
│    ├── valuation.py         # Valuation logic
│    └── fraud.py             # Scam detection
│── ui/
│    ├── dashboard.py         # Streamlit/Flask dashboard
│    └── alerts.py            # Email/Telegram alerts
│── utils/
│    └── driver_utils.py      # Shared Botasaurus config
```

## 🛠️ Installation
```bash
git clone https://github.com/Nivek-C94/auction-hunter.git
cd auction-hunter
pip install -r requirements.txt
```

## ▶️ Usage
```bash
python main.py
```

## 📜 License
MIT License
