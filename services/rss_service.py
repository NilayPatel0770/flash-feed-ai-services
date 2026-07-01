import feedparser

from config.database import articles

from services.gemini_service import analyze_article
from services.embedding_service import generate_embedding

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://techcrunch.com/feed/",
    "https://feeds.reuters.com/reuters/topNews"
]

MAX_ARTICLES = 1


def fetch_rss_news():

    inserted = 0
    updated = 0

    for feed_url in RSS_FEEDS:

        print(f"\nFetching: {feed_url}")

        feed = feedparser.parse(feed_url)

        count = 0

        for item in feed.entries:

            if count >= MAX_ARTICLES:
                break

            title = item.get("title", "")
            link = item.get("link", "")

            content = (
                item.get("summary")
                or item.get("description")
                or title
            )
            
            existing = articles.find_one({"url": link})

            # Skip if article is already fully processed
            if (
            existing
            and existing.get("summary")
            and len(existing.get("embedding", [])) > 0
            ):
                print(f"Skipping AI processing: {title}")
                count += 1
                continue

            try:

                ai_result = analyze_article(content)

                summary = ai_result.get("summary", "")
                keywords = ai_result.get("keywords", [])
                sentiment = ai_result.get("sentiment", "Neutral")

            except Exception as e:

                print(f"Gemini Error: {e}")

                summary = ""
                keywords = []
                sentiment = "Neutral"

            try:

                embedding = generate_embedding(content)

            except Exception as e:

                print(f"Embedding Error: {e}")

                embedding = []

            existing = articles.find_one({"url": link})

            if existing:

                articles.update_one(
                    {"url": link},
                    {
                        "$set": {
                            "title": title,
                            "description": content,
                            "content": content,
                            "source": feed.feed.get("title", "RSS"),
                            "summary": summary,
                            "keywords": keywords,
                            "sentiment": sentiment,
                            "embedding": embedding,
                        }
                    }
                )

                updated += 1

                print(f"Updated: {title}")

            else:

                article = {

                    "title": title,
                    "description": content,
                    "content": content,

                    "url": link,

                    "source": feed.feed.get("title", "RSS"),

                    "category": "General",

                    "image": "",

                    "summary": summary,

                    "keywords": keywords,

                    "sentiment": sentiment,

                    "embedding": embedding,

                    "views": 0,

                    "likes": 0,

                    "bookmarks": 0
                }

                articles.insert_one(article)

                inserted += 1

                print(f"Inserted: {title}")

            count += 1

    return {
        "inserted": inserted,
        "updated": updated
    }