#!/usr/bin/env python3
import json
import csv
from collections import defaultdict

logfile = "/var/log/suricata/eve.json"
csvfile = "/var/log/suricata/alert_summary.csv"

rule1_counts = defaultdict(int)
rule2_counts = defaultdict(int)

batch_size = 100
line_counter = 0
batch_number = 1

def print_and_save_summary(batch_number):
    print("\n========================================")
    print(f" Batch {batch_number} Summary (last {batch_size} log entries) ")
    print("========================================")
    print(f"{'Source IP':<20}{'Rule 1 Alerts':<15}{'Rule 2 Alerts':<15}")
    print("-" * 50)

    all_ips = set(rule1_counts.keys()) | set(rule2_counts.keys())
    for ip in all_ips:
        print(f"{ip:<20}{rule1_counts[ip]:<15}{rule2_counts[ip]:<15}")

    notoriety = {ip: rule1_counts[ip] + rule2_counts[ip] for ip in all_ips}
    if notoriety:
        worst_ip = max(notoriety, key=notoriety.get)
        print("\nMost Notorious Attacker:", worst_ip,
              f"(Total Alerts: {notoriety[worst_ip]})")
    else:
        print("\nNo alerts in this batch.")

    print("========================================\n")

    # Append summary to CSV
    with open(csvfile, "a", newline="") as f:
        writer = csv.writer(f)
        # Write header only for first batch
        if batch_number == 1:
            writer.writerow(["Batch", "Source IP", "Rule 1 Alerts", "Rule 2 Alerts", "Total Alerts"])
        for ip in all_ips:
            writer.writerow([batch_number, ip, rule1_counts[ip], rule2_counts[ip], notoriety[ip]])

with open(logfile, "r") as f:
    for line in f:
        try:
            event = json.loads(line)
            if "alert" in event:
                sid = event["alert"].get("sid")
                src = event.get("src_ip")

                if sid == 1000002:  # Rule 1
                    rule1_counts[src] += 1
                elif sid == 1000003:  # Rule 2
                    rule2_counts[src] += 1

            line_counter += 1
            if line_counter >= batch_size:
                print_and_save_summary(batch_number)
                # Reset for next batch
                rule1_counts.clear()
                rule2_counts.clear()
                line_counter = 0
                batch_number += 1
        except json.JSONDecodeError:
            continue
