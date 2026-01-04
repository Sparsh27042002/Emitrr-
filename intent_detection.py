
def detect_intent(text):
    """
    Detects high-level intent from patient dialogue.
    Rule-based (simple & reliable for medical use).
    """

    text_lower = text.lower()

    if any(word in text_lower for word in ["pain", "hurt", "ache", "injury"]):
        return "Report_Symptom"

    if any(word in text_lower for word in ["worried", "anxious", "scared", "concerned"]):
        return "Express_Concern"

    if any(word in text_lower for word in ["treatment", "therapy", "physiotherapy", "medication"]):
        return "Discuss_Treatment"

    if any(word in text_lower for word in ["recover", "better", "improve", "heal"]):
        return "Prognosis_Inquiry"

    return "General_Information"
