from transformers import pipeline

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return f"Sentiment: {result[0]['label']} with confidence: {result[0]['score']:.2f}"
