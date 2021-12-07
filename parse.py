# name, cpu a memory usage, created_at, status a všechny přiřazené IP adresy

import json
from extract import json_extract

# Create a dictionary from sample data
with open("sample-data.json", "r") as data:
    data_list = json.load(data)

# Using extract function to extract values with the key 'name'
names = json_extract(data_list, 'name')
for name in names:
    print(name)

# Extract function does not work in case the given key contains more data structures
config = json_extract(data_list, 'config')
print(config)



