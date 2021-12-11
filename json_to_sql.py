import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import sqlite3
from pprint import pprint
from extract import json_extract

# read json
with open("sample-data.json", "r") as d:
    data = json.load(d)

pprint(data[0])
pprint(data[1])  # TODO delete
print("*" * 80)

print(json_extract(data[0], 'state'))

# little test for the second item
ip_path_exp = parse('state.memory.usage')
if ip_path_exp.find(data[1]):
    for match in ip_path_exp.find(data[1]):
        memory_usage = match.value
else:
    print("Nothing found this time")


db = sqlite3.connect("containers.sqlite")
# db.execute("CREATE TABLE IF NOT EXISTS containers_info (name, cpu_usage, memory_usage, created_at, status)")
db.execute("CREATE TABLE IF NOT EXISTS containers_info (name, cpu_usage, memory_usage)")
db.execute("CREATE TABLE IF NOT EXISTS container_ips (name, ips)")


# search function
def find_item(json_file, json_path):
    parsed_path = parse(json_path)
    if parsed_path.find(json_file):
        for match in parsed_path.find(json_file):
            item = match.value
    else:
        item = None
    return item


for container in data:
    creation_time = find_item(container, 'created_at')
    print(creation_time)

# containers info
for container in data:
    cpu_usage_path_exp = parse('state.cpu.usage')
    if cpu_usage_path_exp.find(container):
        for match in cpu_usage_path_exp.find(container):
            cpu_usage = match.value
            print("CPU usage: {}".format(cpu_usage))
    else:
        cpu_usage = None
        print("No CPU usage here")

# for container in data:
    memory_usage_path_exp = parse('state.memory.usage')
    if memory_usage_path_exp.find(container):
        for match in memory_usage_path_exp.find(container):
            memory_usage = match.value
            print("Memory usage: {}".format(memory_usage))  # TODO delete this
    else:
        memory_usage = None
        print("No memory usage here")  # TODO Delete this

# for container in data:
    name_path_exp = parse('name')
    if name_path_exp.find(container):
        for match in name_path_exp.find(container):
            name = match.value
            print("Name:{}".format(name))  # TODO delete this
    else:
        name = None
        print("No name here")  # TODO delete this
    db.execute("INSERT INTO containers_info VALUES(?, ?, ?)", (name, cpu_usage, memory_usage))



# IPs table
for container in data:
    ip_path_exp = parse('state.network..addresses[0].address')
    name_path_exp = parse('name')
    if ip_path_exp.find(container) and name_path_exp.find(container):
        for match in ip_path_exp.find(container):
            for name in name_path_exp.find(container):
                ip_addresses = match.value
                name = name.value
                print("Name: {}. IP address: {}".format(name, ip_addresses))  # TODO delete this
            db.execute("INSERT INTO container_ips VALUES (?, ?)", (name, ip_addresses))
            db.commit()
    else:
        for name in name_path_exp.find(container):
            name = name.value
        ip_addresses = None
        db.execute("INSERT INTO container_ips VALUES (?, ?)", (name, ip_addresses))
        db.commit()


