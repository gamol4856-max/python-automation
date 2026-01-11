import os

items = os.listdir()

print("FILES:")
for item in items:
    if os.path.isfile(item):
        print("-", item)

print("\nFOLDERS:")
for item in items:
    if os.path.isdir(item):
        print("-", item)
