# Port Scan Analysis  

**Date:** 2025-09-02  
**Interface:** Wi-Fi (en0)  
**Capture File:** captures/portscan.pcapng  

---

## Goal  
To observe the behavior of a port scan and how it appears in Wireshark, including repeated connection attempts across multiple ports and the resulting reset (RST) or no-response behavior.  

---

## Summary Table

| Metric                  | Value                                 |
|--------------------------|---------------------------------------|
| Total Packets            | ~350                                  |
| Protocol Breakdown       | ~41% TCP, ~48% UDP, ~4.6% DNS         |
| Behavior Observed        | Burst of TCP SYN packets              |
| Responses                | Many TCP RST (closed ports)           |
| Suspicious Indicator     | Sequential SYNs = Port Scan signature |


## Observations  

### 1. Packet List (portscan-2025-09-02.pcapng)  
- Shows many TCP SYN packets from the attacker (192.168.0.134) targeting different destination ports.  
- Several ports responded with TCP **RST** (closed ports).  
- This burst of sequential SYNs is characteristic of a port scan.  

---

### 2. Protocol Hierarchy  
TCP dominates the traffic (≈41% of packets), consistent with a SYN scan.  
UDP and DNS appear but are background noise, not part of the scan.  

Screenshot:  
![Protocol Hierarchy](../screenshots/portscan-protocol.png)  

---

### 3. Conversations (Top Talkers)  
- Multiple short-lived TCP conversations were attempted.  
- Many connections ended immediately with **RST**, confirming closed ports.  
- Some connections had no data transfer at all (just SYN + RST).  

Screenshot:  
![Conversations](../screenshots/portscan-conversations.png)  

---

### 4. I/O Graph  
- Clear spikes of traffic within a short time window.  
- The sharp increase in TCP packets followed by RST errors reflects the scanning attempt.  

Screenshot:  
![I/O Graph](../screenshots/portscan-io.png)  

---

## Conclusion  
The capture confirms a **port scanning attempt**:  
- Multiple sequential port probes from a single source IP.  
- Most destination ports immediately reject connections (RST).  
- This behavior is typical of reconnaissance activity before an attack.  
