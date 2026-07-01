from services.embedding_service import generate_embedding

text = """
OpenAI has launched GPT-5.5 with better coding and reasoning.
"""

embedding = generate_embedding(text)

print("Embedding Length:", len(embedding))
print("First 10 values:")
print(embedding[:10])