import os
from datetime import datetime

base_dir = os.getcwd()

for i in range(1, 501):
    folder_path = os.path.join(base_dir, f"company_{i}")
    log_file_path = os.path.join(folder_path, "log.txt")

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file_path, "a") as f:
        f.write(f"[{timestamp}] Automation script ran successfully\n")
