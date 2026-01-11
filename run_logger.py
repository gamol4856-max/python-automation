import os
import platform
from datetime import datetime

log_file = "run_log.txt"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os_name = platform.system()

total_files = len([
    f for f in os.listdir()
    if os.path.isfile(f)
])

with open(log_file, "a") as log:
    log.write(f"[{timestamp}] OS={os_name}, Total_Files={total_files}\n")

print("Log entry written to", log_file)
