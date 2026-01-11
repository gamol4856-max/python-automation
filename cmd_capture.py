import subprocess
from datetime import datetime

output_file = "cmd_output.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

result = subprocess.check_output("dir", shell=True, text=True)

with open(output_file, "w") as f:
    f.write("===== COMMAND OUTPUT =====\n")
    f.write(f"Generated at: {timestamp}\n\n")
    f.write(result)

print("Command output saved to", output_file)
