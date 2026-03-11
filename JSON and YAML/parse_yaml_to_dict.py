import yaml

# open the YAML file
with open("servers.yaml", "r") as file:

    # convert YAML to Python dictionary
    servers = yaml.safe_load(file)

# print the type to confirm conversion
print(type(servers))

# print the dictionary
print(servers)