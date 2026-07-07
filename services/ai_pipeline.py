from services.gemini_service import analyze_article
from services.embedding_service import generate_embedding


def process_article(article):

    print("Generating AI Analysis...")

    ai = analyze_article(article["content"])

    article["summary"] = ai.get("summary", [])

    article["keywords"] = ai.get("keywords", [])

    article["sentiment"] = ai.get("sentiment", "Neutral")

    article["category"] = ai.get("category", "General")

    print("Generating Embedding...")

    article["embedding"] = generate_embedding(
        article["content"]
    )

    return article