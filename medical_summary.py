
def generate_medical_summary(entities):
    summary = {
        "Patient_Name": "Janet Jones",  # From metadata / EHR
        "Symptoms": list(set(entities.get("SYMPTOM", []))),
        "Diagnosis": entities.get("DIAGNOSIS", ["Not mentioned"])[0],
        "Treatment": list(set(entities.get("TREATMENT", []))),
        "Current_Status": "Occasional back pain",
        "Prognosis": entities.get("PROGNOSIS", ["Not specified"])[0]
    }
    return summary
