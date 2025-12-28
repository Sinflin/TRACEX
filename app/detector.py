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
