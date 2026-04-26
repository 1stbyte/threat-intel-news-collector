import feedparser
from datetime import datetime

feeds = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
    "CISA Alerts": "https://www.cisa.gov/uscert/ncas/alerts.xml",
    "SecurityWeek": "https://feeds.feedburner.com/securityweek"
}

print("\nLatest Cybersecurity News\n")
print("=" * 40)

for source, url in feeds.items():
    print(f"\nSource: {source}")
    feed = feedparser.parse(url)

    for entry in feed.entries[:5]:
        print(f"\n{entry.title}")
        print(entry.link)