import os

for i in range(1, 101):
    folder_name = f"batch_{i}"
    if os.path.exists(folder_name):
        os.rmdir(folder_name)
