import yaml
import os

# check all files in current folder
for filename in os.listdir():

    # check only YAML files
    if filename.endswith(".yaml"):

        try:
            with open(filename, "r") as file:
                yaml.safe_load(file)

            print(filename, "is valid")

        except yaml.YAMLError:
            print(filename, "is invalid")