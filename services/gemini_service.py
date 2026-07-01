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
    "sentiment": "Positive"
    }}

    Article:

    {content}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns ```json
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)