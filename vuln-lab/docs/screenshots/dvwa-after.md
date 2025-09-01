# DVWA – Security Scan (After Hardening with Nginx Proxy)

This scan was run against DVWA accessed via an **Nginx reverse proxy** on **http://localhost:8081**, configured with security headers in `default.conf`.

## Summary of Alerts
- **High:** 0
- **Medium:** 2
- **Low:** 6
- **Informational:** 5
- **False Positives:** 0

## Improvements Observed
- Critical missing headers were added:
  - **X-Frame-Options: DENY**
  - **X-Content-Type-Options: nosniff**
  - **Referrer-Policy: no-referrer**
  - **Content-Security-Policy: default-src 'self'**
- Vulnerabilities **reduced from 5 Mediums → 2 Mediums**.
- Most findings downgraded to **Low** or **Informational** severity.
- Stronger protection against clickjacking, MIME sniffing, and content injection.

## Conclusion:  
After adding an Nginx proxy with security headers, the DVWA site showed significantly fewer vulnerabilities. While still intentionally insecure (since DVWA is a training app), this demonstrates how simple header hardening can reduce risk exposure.


