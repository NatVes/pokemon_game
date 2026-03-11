import yaml
import json

# open YAML file
with open("servers.yaml", "r") as yaml_file:

    # convert YAML to dictionary
    data = yaml.safe_load(yaml_file)

# save dictionary as JSON file
with open("servers_from_yaml.json", "w") as json_file:

    json.dump(data, json_file, indent=4)

print("YAML converted to JSON successfully")