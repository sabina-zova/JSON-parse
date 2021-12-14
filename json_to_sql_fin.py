import json
from jsonpath_ng.ext import parse
import sqlite3
import dateutil.parser as dp


db = sqlite3.connect("containers.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS containers_info (name TEXT PRIMARY KEY NOT NULL, cpu_usage INTEGER,"
           "memory_usage INTEGER, created_at TIMESTAMP NOT NULL, status TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS container_ips (name TEXT KEY NOT NULL, ips)")


def find_item(json_dict: dict, json_path: str):
    """Returns an item from the json dictionary using its' json path.
    Should be used for a single item, if the path contains more than 1 item,
    returns only the last item"""
    global item
    parsed_path = parse(json_path)
    if parsed_path.find(json_dict):
        for found in parsed_path.find(json_dict):
            item = found.value
    else:
        item = None
    return item


# read json
with open("sample-data.json", "r") as d:
    data = json.load(d)


# extracting values for the 'containers_info' table
item = None
for container in data:
    name = find_item(container, 'name')
    cpu_usage = find_item(container, 'state.cpu.usage')
    memory_usage = find_item(container, 'state.memory.usage')
    created_at = find_item(container, 'created_at')
    timestamp_created_at = dp.parse(created_at).timestamp()
    status = find_item(container, 'status')
    db.execute("INSERT INTO containers_info VALUES(?, ?, ?, ?, ?)", (name, cpu_usage, memory_usage,
                                                                     timestamp_created_at, status))
    db.commit()


# extracting values for the 'container_ips' table
for container in data:
    ip_path_exp = parse('state.network..addresses[0].address')
    name_path_exp = parse('name')
    if ip_path_exp.find(container) and name_path_exp.find(container):
        name = None
        for match in ip_path_exp.find(container):
            ip_addresses = None
            for name in name_path_exp.find(container):
                ip_addresses = match.value
                name = name.value
            db.execute("INSERT INTO container_ips VALUES (?, ?)", (name, ip_addresses))
            db.commit()
    else:
        for name in name_path_exp.find(container):
            name = name.value
        ip_addresses = None
        db.execute("INSERT INTO container_ips VALUES (?, ?)", (name, ip_addresses))
        db.commit()
