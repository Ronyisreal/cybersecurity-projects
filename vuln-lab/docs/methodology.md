# Methodology (Discover → Assess → Remediate → Rescan)

1) **Discovery**: Nmap sweep (live hosts, ports, service versions).
2) **Assessment**:
   - Network/system: Nessus Essentials or OpenVAS (unauthenticated → authenticated).
   - Web: OWASP ZAP baseline → active (lab only).
   - Containers/filesystem: Trivy (images + fs).
3) **Prioritization**: CVSS v3, exploit maturity, exposure, business impact.
4) **Remediation**: Patch versions, disable unnecessary services, add security headers, rotate weak creds.
5) **Verification**: Re-run the same profiles; compare deltas.
6) **Reporting**: Executive summary + risk register + before/after charts.

Scan tuning & FP handling notes:
- Start safe (baseline/ZAP passive), then increase depth.
- Verify a sample of findings manually (headers, versions).
- Suppress confirmed false positives with rationale.
