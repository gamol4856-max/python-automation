import os

project_path = os.getcwd()

print("===== PROJECT FILE AUDIT =====")
print("Project Path:", project_path)

files = []
folders = []

for item in os.listdir(project_path):
    if os.path.isfile(item):
        files.append(item)
    elif os.path.isdir(item):
        folders.append(item)

print("\nFolders:")
for f in folders:
    print("-", f)

print("\nFiles:")
for f in files:
    print("-", f)

python_files = [f for f in files if f.endswith(".py")]
print("\nTotal Python files:", len(python_files))
