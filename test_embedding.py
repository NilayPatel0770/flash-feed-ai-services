from config.database import articles

article = articles.find_one({
    "embedding": {
        "$exists": True,
        "$ne": []
    }
})

print(len(article["embedding"]))
print(article["embedding"])