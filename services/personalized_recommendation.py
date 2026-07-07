from bson import ObjectId
from config.database import articles
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

EXPECTED_DIMENSION = 384

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

        article_data = dict(article)

        # Convert ObjectId to string
        article_data["_id"] = str(article_data["_id"])

        # Rename url -> sourceUrl for React
        article_data["sourceUrl"] = article_data.get("url", "")

        # Remove fields frontend doesn't need
        article_data.pop("url", None)
        article_data.pop("embedding", None)
        article_data.pop("__v", None)

        # Add recommendation score
        article_data["score"] = float(score)

        recommendations.append(article_data)

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:limit]