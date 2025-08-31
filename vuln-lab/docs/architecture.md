# Architecture & IP Plan

- **Network**: Host-only (e.g., 192.168.56.0/24) or Docker user-defined network `labnet`.
- **Assets**:
  - Metasploitable2 VM — 192.168.56.10
  - Juice Shop — localhost:3000 (or 192.168.56.20 in Docker network)
  - DVWA — localhost:8080 (or 192.168.56.21 in Docker network)
  - Optional Ubuntu VM — 192.168.56.11 (credentialed scans)

Include a diagram (draw.io/Excalidraw) showing subnets and ports discovered.
