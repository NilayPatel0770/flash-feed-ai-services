from services.gemini_service import analyze_article

text = """
OpenAI released GPT-5.5 with major improvements
in coding, reasoning and multilingual support.
"""

result = analyze_article(text)

print(result)