from text_processing.sentiment import analyze_sentiment
from text_processing.ner import extract_entities
from text_processing.summarizer import summarize_text
from image_processing.image_caption import generate_caption
from audio_processing.speech_to_text import convert_speech_to_text

def route_query(query):
    # Sentiment analysis task
    if "sentiment" in query.lower():
        return analyze_sentiment(query)
    # Named Entity Recognition task
    elif "entities" in query.lower() or "named entities" in query.lower():
        return extract_entities(query)
    # Text summarization task
    elif "summarize" in query.lower():
        return summarize_text(query)
    # Image captioning task (assume an image path is provided)
    elif "image" in query.lower():
        return generate_caption(query)
    # Audio to text task (assume an audio file is provided)
    elif "audio" in query.lower():
        return convert_speech_to_text(query)
    else:
        return "Sorry, I can only do sentiment analysis, NER, summarization, image captioning, and speech-to-text right now."

