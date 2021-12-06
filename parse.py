import json

with open("sample-data.json", "r") as data:
    data_list = json.load(data)

for d in data_list:
    print(d)

