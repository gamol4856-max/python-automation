import csv
import json

csv_file = "data.csv"
json_file = "data.json"

data = []

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

print("CSV to JSON conversion completed")
