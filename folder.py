import os

for i in range(1, 101):
    folder_name = f"batch_{i}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
