import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
yaml_data = yaml.dump(source_content)

# 2. Save YAML to a new file
if len(sys.argv) > 2:

    target_file = sys.argv[2]

    if os.path.exists(target_file):
        print("ERROR: " + target_file + " already exists")
        exit(1)

    with open(target_file, "w") as file:
        file.write(yaml_data)

    print("YAML file created successfully")

else:
    print(yaml_data)