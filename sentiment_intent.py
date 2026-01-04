from transformers import pipeline

# Force PyTorch backend
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)

def classify_sentiment(text):
    """
    Classifies sentiment of the input text.
    Returns label and confidence score.
    """
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 3)
    }
