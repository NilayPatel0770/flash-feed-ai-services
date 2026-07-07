import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_article(content):

    prompt = f"""
You are an AI News Analyzer.

Analyze the following news article.

Return ONLY valid JSON.

{{
    "summary": [
        "Point 1",
        "Point 2",
        "Point 3"
    ],
    "keywords": [
        "keyword1",
        "keyword2",
        "keyword3",
        "keyword4",
        "keyword5"
    ],
    "sentiment": "Positive",
    "category": "Technology"
}}

Choose category ONLY from:

Technology
Business
Sports
Health
Science
Politics
Entertainment
Artificial Intelligence
Cyber Security
Startups
General

Article:

{content}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)