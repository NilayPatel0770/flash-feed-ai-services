from services.recommendation_service import recommend_articles

ARTICLE_ID = "6a43af974f5b073635af3da4"

result = recommend_articles(ARTICLE_ID)

print("=" * 50)

print("Recommendations")

print("=" * 50)

for article in result:

    print(article["title"])

    print(article["score"])

    print()