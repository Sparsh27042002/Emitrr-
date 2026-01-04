
def generate_soap_note(entities, summary, sentiment, intent):
    """
    Generate a SOAP note from extracted NLP outputs.
    """

    soap_note = {
        "Subjective": {
            "Patient_Reported_Symptoms": summary.get("Symptoms", []),
            "Patient_Concerns": sentiment["label"],
            "Intent": intent
        },
        "Objective": {
            "Clinical_Findings": entities
        },
        "Assessment": {
            "Diagnosis": summary.get("Diagnosis", "Not mentioned"),
            "Current_Status": summary.get("Current_Status", "Not specified"),
            "Prognosis": summary.get("Prognosis", "Not specified")
        },
        "Plan": {
            "Treatment": summary.get("Treatment", []),
            "Follow_Up": "As advised by physician"
        }
    }

    return soap_note
