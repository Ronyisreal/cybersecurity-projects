# Demo Talk-Track (3–5 minutes)

- **Goal:** show a repeatable vuln mgmt cycle: discover → assess → remediate → rescan → document.
- **Lab:** Juice Shop (3000), DVWA (8080), Nginx proxy (8081).
- **Discovery:** Nmap confirms only intended ports.
- **Assessment:** ZAP baseline/full identify weak/missing headers and typical DVWA vulns.
- **Remediation:** Put nginx in front of DVWA; enforce CSP/XFO/Nosniff/Referrer-Policy.
- **Rescan:** ZAP baseline via proxy shows improved posture (PASS = 56, fewer header warnings).
- **Outcome:** measurable reduction in findings; pattern is reusable for other apps.
