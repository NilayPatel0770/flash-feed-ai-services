from services.gemini_service import (
    generate_summary,
    generate_keywords,
    analyze_sentiment
)

text = """
OpenAI has announced GPT-5.5, a next-generation AI model with improved
reasoning, coding assistance, multilingual capabilities, and faster responses.
The model is expected to help developers build smarter AI applications.
"""

print("=" * 60)
print("🚀 Testing Gemini AI Service")
print("=" * 60)

try:
    print("\n📝 Generating Summary...\n")
    summary = generate_summary(text)
    print(summary)

    print("\n🔑 Extracting Keywords...\n")
    keywords = generate_keywords(text)
    print(keywords)

    print("\n😊 Analyzing Sentiment...\n")
    sentiment = analyze_sentiment(text)
    print(sentiment)

    print("\n" + "=" * 60)
    print("✅ All Gemini Functions Working Successfully")
    print("=" * 60)

except Exception as e:
    print("\n❌ ERROR")
    print(type(e).__name__)
    print(e)