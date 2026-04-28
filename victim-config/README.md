## 📂 Victim Configuration (`victim-config/`)

This folder contains all configuration files used on the **Lubuntu victim machine**. These files define how Suricata monitors traffic and applies custom rules to detect HTTP flood attacks.

---

### 🔹 Files Included

- **`local.rules`**  
  - **System location:** `/var/lib/suricata/rules/local.rules`  
  - **Purpose:** Contains custom Suricata rules for detecting HTTP floods.  
  - **Rules included:**
    - **Rule 1 (SID 1000002):** Always alerts on HTTP traffic to the victim server.  
    - **Rule 2 (SID 1000003):** Alerts only when a source sends ≥100 HTTP requests within 10 seconds (thresholded flood detection).  
  - These rules simulate enterprise detection strategies: one for visibility, one for thresholded alerts to reduce noise.

- **`suricata.yaml`**  
  - **System location:** `/etc/suricata/suricata.yaml`  
  - **Purpose:** Main Suricata configuration file.  
  - **Key settings:**
    - **Interface:** Configured to listen on `enp0s8` (victim’s network interface).  
    - **Rule files:** Includes `local.rules` so custom rules are loaded.  
    - **Logging:** Outputs alerts to `/var/log/suricata/eve.json` (JSON format) and `/var/log/suricata/fast.log` (plain text).  
  - This file ensures Suricata is correctly tied to the victim’s interface and custom rules.

---

### 🔹 How These Files Fit Into the Lab

1. **Apache Web Server** runs on the victim (`192.168.56.12`).  
2. **Suricata** monitors traffic on `enp0s8`.  
3. **Custom Rules** in `local.rules` detect floods against Apache.  
4. **Logs** are written to `eve.json` and `fast.log`.  
5. **Python Scripts** (in `scripts/`) read these logs, summarise alerts, and classify attacker IPs.

---

### 🔹 Usage

- To apply changes after editing rules/configs:
  ```bash
  sudo systemctl restart suricata
