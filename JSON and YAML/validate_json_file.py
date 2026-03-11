import os
import sys
import json

if len(sys.argv) > 1:
    # check file exists
    if os.path.exists(sys.argv[1]):
        # open file for reading
        file = open(sys.argv[1], "r")
        # parse the JSON file - if it loads then the file contains valid JSON
        json.load(file)
        file.close()
        print("JSON file is valid!")
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + sys.argv[1] + "' not found")
else:
    print("ERROR: No JSON file was specified to check")
    print(f"Usage: {sys.argv[0]} <JSON filename>")