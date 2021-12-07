# name, cpu a memory usage, created_at, status a všechny přiřazené IP adresy

import json
from pprint import pprint

# Create a dictionary from sample data
with open("sample-data.json", "r") as data:
    data_list = json.load(data)

# Printing data list type
print(type(data_list))
# Printing data list length
print(len(data_list))
# Beautifuly printing first item in a list
first_item = data_list[0]
pprint(first_item)
# Printing first item type
print(type(first_item))
# Searching for the first required item 'name' in  a first item dict
for k, v in first_item.items():
    if k == 'name':
        print(v)

# Searching for the second required item 'cpu usage' in a first item dict





