## ⚔️ Attacker Setup (`attacker/`)

This folder documents the setup of the **Kali Linux attacker machine** and Docker containers used to generate distributed HTTP flood traffic against the Lubuntu victim.

---

### 🔹 Attacker Environment

- **Host:** Kali Linux VM (`192.168.56.40`)  
- **Interface:** `eth1` (host‑only adapter)  
- **Docker Network:** `192.168.100.0/24` (attacker containers)  
- **Victim Target:** Lubuntu (`192.168.56.12`) running Apache2

---

### 🔹 Setup and Networking

Install Docker and Docker Compose:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
