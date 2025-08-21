from transformers import pipeline

# Load QA model
def load_model():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

