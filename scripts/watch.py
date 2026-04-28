#!/usr/bin/env python3
import json

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

logfile = "/var/log/suricata/eve.json"

# Professional ALERT banner
FLOOD_BANNER = f"""
{RED}========================================{RESET}
{RED}              ALERT TRIGGERED            {RESET}
{RED}========================================{RESET}
"""

print(f"{CYAN}=== Suricata HTTP Flood Monitor (Rule 2 Only) ==={RESET}")

with open(logfile, "r") as f:
    f.seek(0, 2)  # jump to end of file
    while True:
        line = f.readline()
        if not line:
            continue
        try:
            event = json.loads(line)
            if "alert" in event:
                sid = event["alert"].get("sid")
                signature = event["alert"].get("signature")

                # Track ONLY Rule 2 (sid=1000003)
                if sid == 1000003 or signature == "Custom HTTP Flood Threshold Exceeded":
                    src = event.get("src_ip")
                    dest = event.get("dest_ip")
                    ts = event.get("timestamp")

                    # Print banner + colorized alert
                    print(FLOOD_BANNER)
                    print(f"[ALERT] {signature}\n"
                          f"Time: {GREEN}{ts}{RESET}\n"
                          f"Attacker: {RED}{src}{RESET} -> Victim: {CYAN}{dest}{RESET}\n")
        except json.JSONDecodeError:
            continue
