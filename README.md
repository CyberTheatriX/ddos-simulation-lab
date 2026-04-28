# 🛡️ DDoS Simulation Lab

A reproducible lab environment for simulating **distributed HTTP flood attacks** and detecting them with **Suricata IDS**.  
This project integrates **Kali Linux (attacker)**, **Lubuntu (victim)**, **Docker containers**, and **custom Suricata rules**, with monitoring and analysis scripts.

---

## 🔹 Lab Architecture

- **Victim (Lubuntu VM)**  
  - IP: `192.168.56.12`  
  - Service: Apache2 web server  
  - Suricata IDS listening on `enp0s8`  
  - Logs: `/var/log/suricata/eve.json`, `/var/log/suricata/fast.log`

- **Attacker (Kali Linux VM)**  
  - IP: `192.168.56.40`  
  - Interface: `eth1` (host-only adapter)  
  - Docker swarm: `192.168.100.0/24` (10 attacker containers)  
  - Tools: ApacheBench (`ab`) for HTTP flood generation

- **Networking**  
  - IP forwarding enabled on Kali  
  - Proxy ARP + promiscuous mode for macvlan bridging  
  - Forwarding rules allow attacker subnet → victim subnet  
  - **No NAT masquerade** → victim sees real container IPs

---

## 🔹 Components

- **`victim-config/`** → Suricata setup, custom rules, Apache2 configs  
- **`attacker/`** → Kali + Docker setup, macvlan, iptables, attack commands  
- **`scripts/`** → Python utilities (`watch.py`, `summarise.py`) for log monitoring and summarization  
- **`apache2/`** → Victim web server configuration

---

## 🔹 Attacker Workflow

### Build attacker image
```bash
docker build -t attacker-image .
```
### Launch swarm (10 containers)
```bash
docker-compose up -d
```
### Execute baseline attack
```bash
sudo bash -c 'for i in $(seq 10 19); do docker exec attacker$i ab -n 50 -c 3 http://192.168.56.12/ & done; wait'
```

### Execute flood to trigger Suricata Rule 2
```bash
sudo bash -c 'for i in $(seq 10 19); do docker exec attacker$i ab -n 500 -c 20 http://192.168.56.12/ & done; wait'
```
### Detection and monitoring
```bash
tail -f /var/log/suricata/fast.log
```
# Purpose
**This lab demonstrates:**

 - How distributed HTTP floods appear in victim logs.
 - How Suricata rules can distinguish normal traffic vs. flood conditions.
 - How to orchestrate attacks with Docker while preserving real source IP visibility.
 - How to document and reproduce a professional SIEM workflow.
