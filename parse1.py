# name, cpu a memory usage, created_at, status a všechny přiřazené IP adresy

import json
from pprint import pprint
from extract import json_extract

# Create a dictionary from sample data
with open("sample-data.json", "r") as data:
    data_list = json.load(data)

# Printing data list type
print(type(data_list))  # TODO delete this later
# Printing data list length
print(len(data_list))  # TODO delete this later
# Testing the first item
first_item = data_list[0]
# pprint(first_item)
# Printing first item type
print(type(first_item))
# Printing the first required value 'name'
print("Name: {}".format(first_item['name']))
# Printing the second required value 'cpu usage'
print("CPU usage: {}".format(first_item['state']['cpu']['usage']))
# Printing the third required value 'memory usage'
print("Memory usage: {}".format(first_item['state']['memory']['usage']))
# Printing the fourth required value 'created_at'
print("Created at: {}".format(first_item['created_at']))
# Printing the fifth required value 'status'
print("Status: {}".format(first_item['status']))
# Printing the last required value 'ip addresses'
for item in first_item['state']['network']['br-853f262736e0']['addresses']:
    print("IP address: {}".format(item['address']))

print("*" * 80)

# Testing the second item
# second_item = data_list[1]
# pprint(second_item)
# print("*" * 80)
# print("Name: {}".format(second_item['name']))
# # print("CPU usage: {}".format(second_item['state']['cpu']['usage']))
# print("Memory usage: {}".format(second_item['state']['memory']['usage']))
# print("Created at: {}".format(second_item['created_at']))
# print("Status: {}".format(second_item['status']))
# for item in second_item['state']['network']['br-853f262736e0']['addresses']:
#     print("IP address: {}".format(item['address']))

print("*" * 80)

# Testing the third item (IP address with 'json_extract')
# third_item = data_list[2]
# pprint(third_item)
# print("*" * 80)
# print("Name: {}".format(third_item['name']))
# print("CPU usage: {}".format(third_item['state']['cpu']['usage']))
# print("Memory usage: {}".format(third_item['state']['memory']['usage']))
# print("Created at: {}".format(third_item['created_at']))
# print("Status: {}".format(third_item['status']))
# ip_addresses = json_extract(third_item, 'address')
# for address in ip_addresses:
#     print(address)
#
#
# print("*" * 80)

# Testing the fourth item with 'json_extract' method
fourth_item = data_list[3]
pprint(fourth_item)
print("*" * 80)
print("Name: {}".format(json_extract(fourth_item, 'name')))
print("CPU usage: {}".format(fourth_item['state']['cpu']['usage']))
print("Memory usage: {}".format(fourth_item['state']['memory']['usage']))
print("Created at: {}".format(fourth_item['created_at']))
print("Status: {}".format(fourth_item['status']))
ip_addresses = json_extract(fourth_item, 'address')
for address in ip_addresses:
    print(address)


print("*" * 80)





