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
