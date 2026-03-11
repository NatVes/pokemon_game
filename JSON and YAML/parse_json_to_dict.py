import json

# open the JSON file
with open("servers.json", "r") as jsonfile:

    # convert JSON file to Python dictionary
    servers = json.load(jsonfile)
    # convert JSON string to Python dictionary:
    # servers = json.loads(json_str)

# print the type
print(type(servers))

# print server1
print(servers["server1"])

# print server2
print(servers["server2"])

#Part 2
#loop through all servers
for key, value in servers.items():

    print("Key and value:", key, "=", value)

    # loop through the inner dictionary
    for subkey, subvalue in value.items():
        print("  Record key and sub value:", subkey, "=", subvalue)