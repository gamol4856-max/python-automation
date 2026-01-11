import os
from datetime import datetime

report_file = "clean_report.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

files = []
folders = []

for item in os.listdir():
    if item == "venv":
        continue
    if os.path.isfile(item):
        files.append(item)
    elif os.path.isdir(item):
        folders.append(item)

py_files = [f for f in files if f.endswith(".py")]

with open(report_file, "w") as r:
    r.write("===== CLEAN PROJECT REPORT =====\n")
    r.write(f"Generated at: {timestamp}\n\n")

    r.write("Folders:\n")
    for f in folders:
        r.write(f"- {f}\n")

    r.write("\nFiles:\n")
    for f in files:
        r.write(f"- {f}\n")

    r.write(f"\nTotal Python files: {len(py_files)}\n")

print("Clean report generated:", report_file)
print("Python files:", len(py_files))
