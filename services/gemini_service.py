import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_article(content):

    prompt = f"""
You are an AI news assistant.

Analyze the following news article and return ONLY valid JSON.

Format:

{{
    "summary":"3 concise bullet points",
    "keywords":["keyword1","keyword2","keyword3","keyword4","keyword5"],
    "sentiment":"Positive"
}}

Sentiment must be one of:
Positive
Negative
Neutral

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