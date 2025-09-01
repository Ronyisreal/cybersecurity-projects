# Baseline Traffic Analysis

**Date:** 2025-09-02  
**Interface:** Wi-Fi (en0)  
**Duration:** ~1 minute capture during normal browsing activity  

---

## Goal
Establish a baseline of **normal network traffic** for comparison against future security scenarios (e.g., scans, anomalies, exfiltration).

---

## Observations

### 1. Protocol Hierarchy
- **IPv4 traffic dominates** (~99%)  
- Majority carried via **TCP (45%)** and **UDP (54%)**  
- Inside TCP: most flows are **TLS-encrypted HTTPS (port 443)**  
- A small amount of **DNS queries (UDP/53)** present  
- Minimal ARP/ICMP — expected for local network  

Screenshot: [Protocol Hierarchy](../screenshots/baseline-protocol.png)

---

### 2. Conversations (Top Talkers)
- The largest data exchange was between **local IP (192.168.x.x)** and an external IP (17.x.x.x, Apple CDN/YouTube/etc.)  
- Data volumes in MB range → consistent with video streaming or software updates  
- Other minor connections: DNS resolvers and multicast traffic  

Screenshot: [Conversations](../screenshots/baseline-conversations.png)

---

### 3. I/O Graph
- Normal browsing produced **spikes of 600–800 packets/sec** during bursts (likely video or page loads)  
- TCP errors appear occasionally (retransmissions, resets), but low volume → normal in Wi-Fi environments  
- Background traffic remained <100 packets/sec  

Screenshot: [I/O Graph](../screenshots/baseline-io.png)

---

## Key Takeaways
- Normal home baseline = **mostly HTTPS/TLS** with **occasional DNS + multicast**  
- Short bursts of high packet rates are expected with video/streaming  
- Low, isolated TCP errors = normal on Wi-Fi  
- This baseline will serve as a **reference point** for detecting anomalies (spikes in DNS errors, SYN floods, odd User-Agents, or unexplained bulk transfers)

---


