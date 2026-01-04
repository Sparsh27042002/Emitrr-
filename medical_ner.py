import spacy

nlp = spacy.load("en_core_web_sm")

def extract_medical_entities(text):
    """
    Extract medical-related entities from text.
    Returns a dictionary grouped by entity label.
    """
    doc = nlp(text)

    entities = {}
    for ent in doc.ents:
        entities.setdefault(ent.label_, []).append(ent.text)

    return entities
