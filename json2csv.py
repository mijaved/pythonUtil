/*
Ref: https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
*/

import csv, json, sys

input = open("json2csv_division.json")
data = json.load(input)
input.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys())  # header row

for row in data:
    output.writerow(row.values())