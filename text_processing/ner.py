from transformers import pipeline

def extract_entities(text):
    ner_pipeline = pipeline("ner")
    result = ner_pipeline(text)
    entities = [f"{entity['word']} ({entity['label']})" for entity in result]
    return "Entities: " + ", ".join(entities)
