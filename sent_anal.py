from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (one-time requirement)
nltk.download("vader_lexicon")

def analyze_sentiment_vader(text):
    """Analyzes sentiment using VADER (Positive, Negative, or Neutral)."""
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage
text = "Tesla's latest earnings report was bad with record-breaking sales!"
print("VADER Sentiment:", analyze_sentiment_vader(text))