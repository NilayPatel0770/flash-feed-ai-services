from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["ai_news_db"]

articles = db["articles"]
users = db["users"]
categories = db["categories"]

print("MongoDB Connected")