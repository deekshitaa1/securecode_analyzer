
import re

def detect_sql_injection(code):
    patterns = [
        r"SELECT.*\+",
        r"INSERT.*\+",
        r"UPDATE.*\+",
    ]
    findings = []
    for p in patterns:
        for m in re.finditer(p, code, re.IGNORECASE):
            findings.append({"issue": "Possible SQL Injection", "line": code.count("\n", 0, m.start())+1})
    return findings

def detect_secrets(code):
    patterns = [
        r"AKIA[0-9A-Z]{16}",
        r"secret_key\s*=\s*['\"]",
    ]
    findings = []
    for p in patterns:
        for m in re.finditer(p, code):
            findings.append({"issue": "Hardcoded Secret", "line": code.count("\n", 0, m.start())+1})
    return findings

def detect_insecure_api(code):
    patterns = [
        r"verify=False",
        r"md5\(",
    ]
    findings = []
    for p in patterns:
        for m in re.finditer(p, code):
            findings.append({"issue": "Insecure API Usage", "line": code.count("\n", 0, m.start())+1})
    return findings

def run_scan(code):
    return (
        detect_sql_injection(code)
        + detect_secrets(code)
        + detect_insecure_api(code)
    )
