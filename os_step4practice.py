import os

count = 0

for item in os.listdir():
    if item.endswith(".py") and os.path.isfile(item):
        count = count + 1

print("Total Python files:", count)
