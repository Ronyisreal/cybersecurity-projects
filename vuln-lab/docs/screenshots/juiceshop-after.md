# Juice Shop – After Remediation (ZAP Baseline Scan via Nginx Proxy)

## Summary
The Juice Shop application was re-scanned at `http://host.docker.internal:3000` behind an Nginx proxy with additional **security headers** applied (X-Frame-Options, CSP, Referrer-Policy, etc.).

### Risk Summary
- **High:** 0  
- **Medium:** 2  
- **Low:** 5  
- **Informational:** 5  

### Key Findings (After Remediation)
1. **Content Security Policy (CSP) Header Not Set** – Still flagged as medium risk.  
2. **Cross-Domain Misconfiguration** – Still flagged, though reduced instances.  
3. **Dangerous JS Functions** – Persist (client-side code issue).  
4. **Insufficient Site Isolation Against Spectre** – Still reported.  
5. **Information Disclosure** – Comments remain in source code.  
6. **Storable/Non-Storable Cacheable Content** – Still flagged.  

### Improvements
- Headers like **X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Content-Security-Policy** are now present.  
- No **critical** vulnerabilities.  
- Many **medium issues remain**, but they are mainly due to inherent Juice Shop design.

## Observations
Even after remediation, Juice Shop continues to show multiple **warnings** because it is intentionally insecure. However, the **presence of strong headers reduces risk severity**, demonstrating how a reverse proxy can mitigate web vulnerabilities.

