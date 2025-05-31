# utils/llm.py
from transformers import pipeline
import logging

classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def classify_intent_llm(text: str) -> str:
    try:
        result = classifier(text[:512])  # Truncate long inputs
        label = result[0]['label']
        # Simple mapping to intents
        if label in ['joy', 'surprise']:
            return "RFQ"
        elif label in ['anger', 'sadness']:
            return "Complaint"
        elif label in ['fear']:
            return "Regulation"
        else:
            return "General"
    except Exception as e:
        logging.error(f"LLM classification error: {e}")
        return "Unknown"
