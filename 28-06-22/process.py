import csv
# https://ellibrodepython.com/context-managers-python
with open("datacamp_catalog.csv", encoding="utf-8") as csv_file:
    file_to_process = csv.DictReader(csv_file)
    for i  in file_to_process:
        print(i["CPNT_ID"], i["CPNT_TITLE"])
        print()
# context
# split
python = []
r = []
data =[]