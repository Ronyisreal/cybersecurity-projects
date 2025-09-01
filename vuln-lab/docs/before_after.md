# Before/After Results

## Targets
- Juice Shop: `http://localhost:3000`
- DVWA (proxied with security headers): `http://localhost:8081` (origin DVWA on `:8080`)

## Evidence

| Tool | Scope | Metric | Before | After | Evidence |
|---|---|---|---:|---:|---|
| Nmap | localhost | Listening app ports | 3000, 8080 | 3000, 8080 *(unchanged)* | `scans/before/02_localports_sV.nmap` |
| ZAP | DVWA | Missing/weak security headers | **High** | **Reduced** | `scans/before/zap-full-dvwa.html` → `scans/after/zap-baseline-dvwa-proxy.html` |
| ZAP | DVWA | Total PASSed checks | – | **56 PASS** | `scans/after/zap-baseline-dvwa-proxy.html` |

### What I changed
- Put **nginx reverse proxy** in front of DVWA and injected headers:
  - `X-Frame-Options: DENY`
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy: no-referrer`
  - `Content-Security-Policy: default-src 'self'`
- Kept apps **bound to localhost** only.

### Why risk is lower
- Common browser-based attacks (clickjacking, MIME sniffing, data exfiltration) are mitigated by the new headers.
- Proxy makes it easy to **standardize controls** in front of legacy apps without modifying the app.

