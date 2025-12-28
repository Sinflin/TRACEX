from fastapi import FastAPI
import json



def generate_report(incident_id, incident_type, evidence, recommendations):
    return {
        "incident_id": incident_id,
        "type": incident_type,
        "severity": "High",
        "evidence": evidence,
        "recommendations": recommendations
    }


def recommend_actions(incident_type):
    if incident_type == "Brute Force Attack":
        return [
            "Block source IP",
            "Reset affected user password",
            "Enable MFA"
        ]
    return ["Monitor system"]


def correlate_incidents(incidents):
    return incidents  # simple correlation for MVP


def collect_evidence(incident, logs):
    related_logs = [
        log for log in logs
        if log.get("ip") == incident.get("ip")
    ]

    return {
        "affected_user": incident["user"],
        "source_ip": incident["ip"],
        "related_logs": related_logs
    }
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


def detect_incidents(logs):
    incidents = []
    failed_logins = {}

    for log in logs:
        if log.get("event") == "login_failed":
            ip = log.get("ip")
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

            if failed_logins[ip] >= 3:
                incidents.append({
                    "type": "Multiple Failed Login Attempts",
                    "ip": ip,
                    "user": log.get("user"),
                    "timestamp": log.get("timestamp")
                })

    return incidents



app = FastAPI(title="Automated Incident Response Platform")

@app.get("/")
def root():
    return {"message": "Incident Response Platform Running"}

@app.post("/analyze_logs")
def analyze_logs():
    with open("data/logs.json") as f:
        logs = json.load(f)

    incidents = detect_incidents(logs)
    correlated = correlate_incidents(incidents)

    reports = []

    for idx, incident in enumerate(correlated):
        incident_type = classify_incident(incident)
        evidence = collect_evidence(incident, logs)
        recommendations = recommend_actions(incident_type)

        report = generate_report(
            incident_id=f"INC-{idx+1}",
            incident_type=incident_type,
            evidence=evidence,
            recommendations=recommendations
        )

        reports.append(report)

    return reports
