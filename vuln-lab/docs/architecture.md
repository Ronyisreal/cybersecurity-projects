# Architecture & IP Plan

This document describes the design of the **Vulnerability Scanning Home Lab**.  
The goal is to provide a contained, repeatable environment for practicing **discovery, assessment, remediation, and rescanning**.

## Network Layout

- **Type:** Docker bridge network (default) or custom `labnet` (subnet `172.18.0.0/16`)  
- **Scope:** All assets are isolated on my host machine and not exposed to the public internet.  

## Assets

- **OWASP Juice Shop**
  - A deliberately vulnerable web application  
  - Runs at: `http://localhost:3000` (or `172.18.0.20` if using Docker `labnet`)  
  - Purpose: Practice web application scanning (e.g., OWASP ZAP, Nmap NSE scripts)  

- **DVWA (Damn Vulnerable Web App)**
  - Another intentionally insecure web application  
  - Runs at: `http://localhost:8080` (or `172.18.0.21` if using Docker `labnet`)  
  - Purpose: Test common vulnerabilities such as SQLi, XSS, brute force, and run ZAP active scans  

- **Metasploitable2 (optional VM)**
  - Legacy Linux VM filled with outdated and insecure services  
  - Example IP: `192.168.56.10` (on a host-only subnet)  
  - Purpose: Demonstrate unauthenticated and credentialed vulnerability scans with Nessus/OpenVAS  

- **Ubuntu VM (optional)**
  - Standard Linux VM left intentionally unpatched  
  - Example IP: `192.168.56.11` (on a host-only subnet)  
  - Purpose: Show credentialed scans (via SSH), patch management, and remediation workflow  



## Ports of Interest (discovered via Nmap)

- **3000/tcp** → Juice Shop (Node.js/Express)  
- **8080/tcp** → DVWA (Apache 2.4.25 Debian)  
- Additional ports if VMs are added (e.g., SSH 22/tcp on Ubuntu, FTP/Telnet on Metasploitable2)

