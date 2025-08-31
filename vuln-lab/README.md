# Vulnerability Scanning Home Lab

## Project Goal
Design a small, contained lab that you can **scan, fix, and rescan** to demonstrate real vulnerability management skills: discovery, assessment, prioritization (CVSS + context), remediation, and proof of **risk reduction** with before/after results.

## What I'll build
- A mini network with intentionally vulnerable targets (VMs/containers).
- Automated discovery (Nmap), vuln scans (Nessus/OpenVAS, Trivy), and web DAST (OWASP ZAP).
- A remediation cycle with measurable deltas (critical/high counts down).

## Architecture (high level)
```
Host (Mac)
└── Lab Network (host-only or Docker network)
    ├─ Metasploitable2 VM                [classic vulns]
    ├─ OWASP Juice Shop (Docker)         [web app vulns]
    ├─ DVWA (Docker)                     [web app vulns]
    └─ Optional: Ubuntu VM (outdated)    [credentialed scans]
Tools:
  Nmap, Nessus/OpenVAS, OWASP ZAP, Trivy
```

## Quickstart
1. **Create target containers**
   ```bash
   docker run -d --name juice -p 3000:3000 bkimminich/juice-shop
   docker run -d --name dvwa -p 8080:80 vulnerables/web-dvwa
   ```
2. **Discovery (Nmap)**
   ```bash
   nmap -sn 192.168.56.0/24 -oA scans/01_ping-sweep
   nmap -sS -sV --top-ports 1000 192.168.56.0/24 -oA scans/02_top1k_sV
   ```
3. **Web scans (ZAP)** (baseline first; active only inside lab)
   ```bash
   docker run --rm -t owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000 -r zap-baseline-juice.html
   docker run --rm -t owasp/zap2docker-stable zap-full-scan.py -t http://localhost:8080 -r zap-full-dvwa.html
   ```
4. **Container scans (Trivy)**
   ```bash
   trivy image bkimminich/juice-shop --format table --output trivy-juice.txt
   trivy fs . --scanners vuln,secret --output trivy-fs.txt
   ```
5. **Plan fixes** (see `docs/methodology.md`) and rescan to show deltas.

## Deliverables
- `docs/architecture.md` — diagram + IP plan
- `docs/methodology.md` — steps, tools, tuning choices
- `docs/before_after.md` — charts, key CVEs removed
- `docs/talk-track.md` — 5–8 minute demo script
- `scans/` — sanitized reports (no secrets), both **before** and **after**



