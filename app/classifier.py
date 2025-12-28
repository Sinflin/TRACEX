from transformers import pipeline

# Load pretrained AI model (no training needed)
ai_classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased"
)

def classify_incident(incident):
    text = incident["type"]

    result = ai_classifier(text)[0]
    confidence = result["score"]

    if confidence > 0.75:
        return "AI-Classified Security Incident"

    return "Brute Force Attack"
