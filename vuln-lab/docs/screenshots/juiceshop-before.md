 Juice Shop – Before Remediation (ZAP Baseline Scan)

## Summary
The OWASP Juice Shop application was scanned at `http://host.docker.internal:3000` without any additional security headers.  
The ZAP scan revealed multiple **medium**, **low**, and **informational** issues.

### Risk Summary
- **High:** 0  
- **Medium:** 2  
- **Low:** 5  
- **Informational:** 5  

### Key Findings
1. **Content Security Policy (CSP) Header Not Set** – Missing CSP increases the risk of XSS.  
2. **Cross-Domain Misconfiguration** – Application allows cross-domain interactions.  
3. **Cross-Domain JavaScript Source File Inclusion** – Possible injection risk.  
4. **Dangerous JavaScript Functions** – `eval()` and similar functions detected.  
5. **Deprecated Feature Policy Header Set** – Outdated header usage.  
6. **Insufficient Site Isolation Against Spectre** – Potential side-channel leakage.  
7. **Information Disclosure via Comments** – Sensitive information found in HTML comments.  
8. **Non-Storable and Storable Cacheable Content** – Poor caching policies.  
9. **Modern Web Application Warnings** – Best practice deviations.  

## Observations
Juice Shop starts with many client-side vulnerabilities typical of an intentionally insecure application. No critical issues were found, but several **medium risks** remain.
