import os
import platform
from datetime import datetime

report_file = "system_report.txt"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

files = [f for f in os.listdir() if os.path.isfile(f)]
folders = [f for f in os.listdir() if os.path.isdir(f)]

with open(report_file, "w") as report:
    report.write("===== SYSTEM REPORT =====\n")
    report.write(f"Generated at: {timestamp}\n\n")

    report.write("OS Information:\n")
    report.write(f"System: {platform.system()}\n")
    report.write(f"Release: {platform.release()}\n\n")

    report.write("Folders:\n")
    for f in folders:
        report.write(f"- {f}\n")

    report.write("\nFiles:\n")
    for f in files:
        report.write(f"- {f}\n")

print("Report generated:", report_file)
print("Total files:", len(files))
print("Total folders:", len(folders))
