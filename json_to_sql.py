import json
import sqlite3
from pprint import pprint

# creating a connection
conn = sqlite3.connect("sample_data.sqlite")
cursor = conn.cursor()

# read json
with open("sample-data.json", "r") as d:
    data = json.load(d)

pprint(data[0])  # TODO delete

# creating a table
cursor.execute("CREATE TABLE IF NOT EXISTS data (name ID PRIMARY KEY NOT NULL, info json)")

# inserting a json data
for container in data:
    cursor.execute("INSERT INTO data VALUES (?, ?)",
                   [container['name'], json.dumps(container)])
    conn.commit()

pprint(cursor.execute("SELECT json_extract(info, '$.status', '$.created_at',"
                      "'$.state.cpu.usage', '$.state.memory.usage', '$.devices') FROM data").fetchall())





