import os
import platform
import subprocess
from datetime import datetime

report = "daily_report.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

files = [f for f in os.listdir() if os.path.isfile(f) and f != report]
folders = [f for f in os.listdir() if os.path.isdir(f) and f != "venv"]

cmd_output = subprocess.check_output("dir", shell=True, text=True)

with open(report, "w") as r:
    r.write("===== DAILY AUTOMATION REPORT =====\n")
    r.write(f"Generated at: {timestamp}\n\n")

    r.write("OS INFO:\n")
    r.write(f"System: {platform.system()}\n")
    r.write(f"Release: {platform.release()}\n\n")

    r.write("PROJECT SUMMARY:\n")
    r.write(f"Total Files: {len(files)}\n")
    r.write(f"Total Folders: {len(folders)}\n\n")

    r.write("COMMAND OUTPUT (dir):\n")
    r.write(cmd_output)

print("Daily report generated:", report)
