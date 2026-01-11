import csv
import json

csv_file = "emp_data.csv"
js_file = "hr_bkp_jsn.json"

data = []

with open (csv_file , "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)                                      
       # print(row)                                         checking csv file reading


with open (js_file, "w") as f:
    json.dump(data, f, indent=4)
    print("HR data in json format successfully converted")