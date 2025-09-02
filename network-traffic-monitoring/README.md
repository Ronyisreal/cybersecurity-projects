# Network Traffic Monitoring & Analysis

**Date:** September 2025  
**Tools:** Wireshark, tcpdump  

---

## Project Overview  
This project demonstrates the use of **Wireshark** to capture and analyze real-world network traffic.  
The goal is to learn how to:  
- Establish a **baseline of normal traffic**  
- Detect **anomalies in DNS**  
- Compare **HTTP vs HTTPS security**  
- Observe patterns in **large file transfers**  
- Identify **port scanning attempts**  
- Spot **suspicious User-Agent requests**  

Each scenario includes:  
- A `.pcapng` capture file (local only – not uploaded due to size limits)  
- **Screenshots** (protocol hierarchy, conversations, I/O graphs)  
- **Markdown reports** documenting findings  

---

## Project Structure  

network-traffic-monitoring/
│── captures/ # Raw capture files (.pcapng)
│── reports/ # Markdown analysis reports
│ ├── baseline.md
│ ├── dns-anomalies.md
│ ├── http-vs-https.md
│ ├── large-transfer.md
│ ├── portscan.md
│ └── suspicious-ua.md
│── screenshots/ # Wireshark screenshots
│── README.md # Project documentation


---

## 📑 Reports  

| Report | Description |
|--------|-------------|
| [Baseline Traffic](reports/baseline.md) | Establishes normal browsing traffic (reference point). |
| [DNS Anomalies](reports/dns-anomalies.md) | Identifies NXDOMAIN and unusual DNS behaviors. |
| [HTTP vs HTTPS](reports/http-vs-https.md) | Compares unencrypted HTTP with encrypted HTTPS/TLS. |
| [Large Transfer](reports/large-transfer.md) | Observes characteristics of bulk data transfer. |
| [Port Scan](reports/portscan.md) | Detects SYN scans via repeated TCP connection attempts. |
| [Suspicious User-Agent](reports/suspicious-ua.md) | Flags unusual/malicious HTTP User-Agent strings. |

---

## 🚀 How to Reproduce  

1. **Capture traffic with tcpdump or Wireshark**:  
   ```bash
   sudo tcpdump -i en0 -w capture.pcapng


