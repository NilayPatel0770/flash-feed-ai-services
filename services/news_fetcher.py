import feedparser
from newspaper import Article
from services.ai_pipeline import process_article
from services.rss_service import RSS_FEEDS
from services.article_service import (
    article_exists,
    save_article
)

# BBC_RSS = "https://feeds.bbci.co.uk/news/rss.xml"


def fetch_news():
    saved_articles = []
    MAX_NEW_ARTICLES = 20
    saved_count = 0
    for rss in RSS_FEEDS:

        print("\n==============================")
        print(f"Fetching {rss['source']}")
        print("==============================")

        feed = feedparser.parse(rss["url"])

        print(f"Found {len(feed.entries)} articles")


    for item in feed.entries:

        try:

            # Skip duplicate articles
            if article_exists(item.link):

                print(f"Already Exists: {item.title}")

                continue

            print(f"Downloading: {item.title}")

            article = Article(item.link)

            article.download()

            article.parse()

            article_data = {

                "title": article.title,

                "description": item.summary,

                "content": article.text,

                "image": article.top_image,

                "author": ", ".join(article.authors),

                "source": rss["source"],

                "sourceUrl": item.link,

                "category": rss["category"],

                "publishedAt": item.published,

                # AI Fields (will fill later)

                "summary": [],

                "keywords": [],

                "embedding": [],

                "sentiment": "Neutral",

                # Statistics

                "views": 0,

                "likes": 0,

                "bookmarks": 0,

            }
            
            article_data = process_article(article_data)

            save_article(article_data)
            saved_count += 1
            if saved_count >= MAX_NEW_ARTICLES:
                print("Daily processing limit reached.")
                return saved_articles
            saved_articles.append(article_data)

            print(f"Saved: {article.title}")

        except Exception as e:

            print("-----------------------------------")
            print(f"Failed: {item.link}")
            print(e)
            print("-----------------------------------")

    print(f"\nTotal New Articles Saved: {len(saved_articles)}")

    return saved_articles