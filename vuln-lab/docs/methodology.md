# Methodology (Discover → Assess → Remediate → Rescan)

1) **Discovery (Nmap)**
   ```bash
   sudo nmap -sS -sV -p 3000,8080 localhost -oA scans/before/02_localports_sV
