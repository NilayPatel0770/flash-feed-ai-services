from bson import ObjectId
from config.database import articles
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def recommend_articles(article_id, limit=10):

    article = articles.find_one(
        {"_id": ObjectId(article_id)}
    )

    if not article:
        return []

    current_embedding = article.get("embedding", [])

    if len(current_embedding) == 0:
        return []

    recommendations = []

    cursor = articles.find({
        "_id": {"$ne": ObjectId(article_id)}
    })

    for news in cursor:

        embedding = news.get("embedding", [])

        if len(embedding) == 0:
            continue

        score = cosine_similarity(
            np.array(current_embedding).reshape(1, -1),
            np.array(embedding).reshape(1, -1)
        )[0][0]

        recommendations.append({

            "_id": str(news["_id"]),

            "title": news["title"],

            "category": news.get("category", ""),

            "summary": news.get("summary", ""),

            "image": news.get("image", ""),

            "score": round(float(score), 4)

        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:limit]