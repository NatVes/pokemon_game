import json

# open JSON file
with open("servers.json", "r") as jsonfile:

    # Read the JSON file content as a string
    json_str = jsonfile.read()

    # Convert JSON string into a Python dictionary
    servers = json.loads(json_str)

print(type(servers))
print(servers)