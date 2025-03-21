import requests
import dateparser
import streamlit as st
import spacy
from sent_anal import analyze_sentiment_vader

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_topics(text):
    """Extracts key topics (Named Entities) from text using spaCy."""
    doc = nlp(text)
    topics = {ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT", "EVENT"]}  # Extract orgs, places, and products
    return list(topics) if topics else ["No key topics identified"]

def fetch_news(company, num_articles=10):
    """Fetches at least 10 news articles related to the given company using NewsAPI."""
    API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with your actual API key
    search_url = f"https://newsapi.org/v2/everything?q={company}&language=en&sortBy=publishedAt&pageSize={num_articles}&apiKey={API_KEY}"
    
    response = requests.get(search_url)
    if response.status_code != 200:
        st.error("Error fetching news articles")
        return []
    
    news_data = response.json()
    articles = []
    
    for item in news_data.get("articles", []):
        title = item.get("title", "No title")
        summary = item.get("description", "No summary")
        link = item.get("url", "")
        source = item.get("source", {}).get("name", "Unknown source")
        timestamp = dateparser.parse(item.get("publishedAt", "")) if item.get("publishedAt") else "Unknown timestamp"
        
        # Extract sentiment analysis
        sentiment = analyze_sentiment_vader(summary)
        
        # Extract topics using spaCy NER
        topics = extract_topics(summary)
        
        if title and summary and link:
            articles.append({
                "title": title,
                "summary": summary,
                "link": link,
                "sentiment": sentiment,
                "source": source,
                "timestamp": timestamp if timestamp else "Unknown timestamp",
                "topics": topics  # Adding extracted topics
            })
    
    return articles