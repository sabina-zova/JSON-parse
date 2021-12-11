import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import sqlite3
from pprint import pprint

# read json
with open("sample-data.json", "r") as d:
    data = json.load(d)


db = sqlite3.connect("containers.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS containers_info (name, cpu_usage, memory_usage, created_at, status)")
# db.execute("CREATE TABLE IF NOT EXISTS containers_info (name, cpu_usage, memory_usage)")
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
    name = find_item(container, 'name')
    cpu_usage = find_item(container, 'state.cpu.usage')
    memory_usage = find_item(container, 'state.memory.usage')
    created_at = find_item(container, 'created_at')
    status = find_item(container, 'status')
    db.execute("INSERT INTO containers_info VALUES(?, ?, ?, ?, ?)", (name, cpu_usage, memory_usage, created_at, status))

print("*" * 80)
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

print("*" * 80)

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
