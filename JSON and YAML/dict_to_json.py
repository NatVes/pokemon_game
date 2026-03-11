import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# convert dictionary to JSON string
json_string = json.dumps(servers_dict)

print (type(json_string))

# save dictionary to JSON file
with open("servers1.json", "w") as file:
    json.dump(servers_dict, file, indent=4)

