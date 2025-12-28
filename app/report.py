def generate_report(incident_id, incident_type, evidence, recommendations):
    return {
        "incident_id": incident_id,
        "type": incident_type,
        "severity": "High",
        "evidence": evidence,
        "recommendations": recommendations
    }
