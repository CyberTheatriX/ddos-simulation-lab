## 📂 Monitoring Scripts (`scripts/`)

This folder contains Python scripts used to monitor and summarise Suricata alerts generated on the Lubuntu victim machine.

---

### 🔹 Files Included

- **`watch.py`**  
  - Purpose: Continuously monitors Suricata’s `eve.json` log file.  
  - Features:
    - Tails the log in real time.  
    - Filters for flood‑related alerts (e.g., SID 1000002 and 1000003).  
    - Prints alerts to the console for immediate visibility.  
  - Usage:
    ```bash
    python3 watch.py
    ```

- **`summarise.py`**  
  - Purpose: Processes Suricata alerts in batches to classify attacker IPs.  
  - Features:
    - Reads alerts from `eve.json`.  
    - Groups alerts by source IP.  
    - Distinguishes between Rule 1 (always‑alert) and Rule 2 (thresholded flood detection).  
    - Outputs a CSV summary for analysis.  
  - Usage:
    ```bash
    python3 summarise.py
    ```

---

### 🔹 How These Scripts Fit Into the Lab

1. Suricata generates alerts when attackers flood Apache.  
2. `watch.py` provides **real‑time visibility** of those alerts.  
3. `summarise.py` provides **post‑attack analysis**, showing which IPs triggered thresholded flood rules.  
4. Together, they demonstrate both **live monitoring** and **forensic summarisation**.

---

✅ This section documents the monitoring scripts that complement the victim configuration, making the lab reproducible and professional.
