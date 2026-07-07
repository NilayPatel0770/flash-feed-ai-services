from newspaper import Article


def extract_article_data(url):

    try:

        article = Article(url)

        article.download()

        article.parse()

        return {
            "image": article.top_image,
            "author": ", ".join(article.authors) if article.authors else "Unknown",
            "content": article.text
        }

    except Exception as e:

        print("Article Parser Error:", e)

        return {
            "image": "",
            "author": "Unknown",
            "content": ""
        }