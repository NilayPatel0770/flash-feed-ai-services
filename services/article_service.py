from config.database import articles


def article_exists(source_url):

    return articles.find_one({
        "sourceUrl": source_url
    }) is not None


def save_article(article):

    result = articles.insert_one(article)

    print(f"Inserted: {result.inserted_id}")

    return result.inserted_id