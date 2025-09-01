# DVWA – Baseline Security Scan (Before Hardening)

This scan was run against the raw DVWA instance exposed directly on **http://localhost:8080** without any reverse proxy or additional headers.

## Summary of Alerts
- **High:** 0
- **Medium:** 5
- **Low:** 7
- **Informational:** 7
- **False Positives:** 0

## Key Issues Detected
- Missing **Content Security Policy (CSP)**
- **Directory Browsing** enabled
- Missing **Anti-Clickjacking Header**
- Cookies without **HttpOnly** / **SameSite** flags
- Server leaks version information
- Insufficient **Spectre vulnerability isolation**
- Multiple missing security headers (X-Content-Type-Options, Permissions Policy)

## Screenshot
![DVWA Before Scan](../docs/screenshots/dvwa-before.png)

**Conclusion:**  
The unprotected DVWA instance is highly insecure and exposes multiple missing header issues and misconfigurations. This demonstrates why web applications must be deployed with proper security headers and reverse proxies.
