# securecode_analyzer
“I built a full end-to-end mini SAST platform called SecureCode Analyzer.
It performs static analysis similar to how Black Duck, Checkmarx, and SonarQube engines work internally.

The scanner is written in Python and it doesn't rely only on regex.
I built an AST-based rule engine that actually understands the code structure.
So instead of searching for keywords, it detects real vulnerabilities like SQL injection by tracking how user inputs flow into database execution statements — a simplified taint analysis model.

For secrets, I implemented high-entropy detection, private-key pattern recognition, and hardcoded credential rules the same way enterprise scanners identify credential leaks.

For insecure API usage, I built rules to detect weak cryptography (MD5, SHA1), insecure HTTP calls, and SSL verification bypass.

All findings are normalized into a JSON format with severity, CWE-style rule IDs, and remediation advice.

On top of the engine, I built a Flask-based Security Dashboard — developers can upload code, trigger scans, and view detailed findings with file location highlighting.

The important part is DevSecOps integration.
I integrated the tool into CI/CD using GitHub Actions so every pull request gets automatically scanned.
Builds fail if new high-severity issues appear.

And I also tied it into SonarQube using external issue imports. That means my scanner’s results show up in SonarQube’s Security Hotspot dashboard and quality gates can block merges based on my tool’s findings.

So in short, I essentially built a lightweight version of a SAST pipeline:
custom rule engine → vulnerability detection → Flask dashboard → CI/CD enforcement → SonarQube Quality Gates.

This project gave me hands-on understanding of how real AppSec tools like Black Duck operate under the hood.”**
