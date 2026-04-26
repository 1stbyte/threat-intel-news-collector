import feedparser
import csv
from datetime import datetime

feeds = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
    "CISA Alerts": "https://www.cisa.gov/uscert/ncas/alerts.xml",
    "SecurityWeek": "https://feeds.feedburner.com/securityweek"
}

filename = "cybersecurity_news.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Title", "Published", "Link"])

    for source, url in feeds.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            published = entry.get("published", "Unknown")
            writer.writerow([source, entry.title, published, entry.link])

print(f"\nNews saved to {filename}")
