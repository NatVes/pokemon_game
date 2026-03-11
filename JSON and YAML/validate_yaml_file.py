import yaml

try:
    # try to open and parse the YAML file
    with open("servers.yaml", "r") as file:
        yaml.safe_load(file)

    print("YAML file is valid")

# if there is an error in the YAML structure
except yaml.YAMLError as e:
    print("YAML file is invalid")
    print(e)