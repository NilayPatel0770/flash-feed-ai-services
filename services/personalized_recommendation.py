from bson import ObjectId
from config.database import articles
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

EXPECTED_DIMENSION = 384

def personalized_recommendations(user_embedding, limit=20):

    if len(user_embedding) != EXPECTED_DIMENSION:
        raise ValueError(
            f"Expected embedding length {EXPECTED_DIMENSION}, got {len(user_embedding)}"
        )

def personalized_recommendations(user_embedding, limit=20):

    recommendations = []

    cursor = articles.find()

    for article in cursor:

        embedding = article.get("embedding", [])

        if len(embedding) == 0:
            continue

        score = cosine_similarity(
            np.array(user_embedding).reshape(1, -1),
            np.array(embedding).reshape(1, -1)
        )[0][0]

        recommendations.append({

            "_id": str(article["_id"]),

            "title": article["title"],

            "category": article.get("category"),

            "summary": article.get("summary"),

            "image": article.get("image"),

            "score": float(score)

        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:limit]