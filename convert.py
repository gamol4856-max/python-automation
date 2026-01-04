import csv
import json


file_path = (r"C:\Users\Amol\company_project\input.csv") # file path for csv file reading

data = []
with open(file_path, "r") as cfile: 
    reader = csv.DictReader(cfile)
    for row in reader:                                   # loop used for read each row
         print (row)
         data.append(row)
 


with open (r"C:\Users\Amol\company_project\out.json" , "w",  newline="", encoding="utf-8",) as jfile:
     
    json.dump(data, jfile, indent=4)
    
print ("json file converion successfully")

