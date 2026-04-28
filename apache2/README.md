## 🌐 Apache2 Web Server (`apache2/`)

The Lubuntu victim machine runs **Apache2** as the target service for HTTP flood attacks in the lab.  
This section documents how Apache2 was installed, configured, tested, and its role in the lab.

---

### 🔹 Apache2 Setup and Role in the Lab

Install Apache2 and confirm it is running:

```bash
sudo apt update
sudo apt install apache2 -y
systemctl status apache2
