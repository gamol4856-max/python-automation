import json

jsn_file = r"C:\Users\Amol\company_project\mywork\hr_bkp_jsn.json"

with open (jsn_file , "r") as f:
     reader = json.load(f)
     print(reader)
