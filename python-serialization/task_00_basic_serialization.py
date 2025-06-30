#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    # Serialize and save to file
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    # Optional: read back the file for verification or display
    with open(filename, "r") as file:
        loaded_data = json.load(file)
    return loaded_data
