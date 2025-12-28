def recommend_actions(incident_type):
    if incident_type == "Brute Force Attack":
        return [
            "Block source IP",
            "Reset affected user password",
            "Enable MFA"
        ]
    return ["Monitor system"]
