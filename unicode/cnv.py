import os
import json

# Get the directory of the current Python file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path for the JSON file in the same directory as the Python file
json_file_path = os.path.join(current_dir, "unicode.json")

# Read data from JSON file
with open(json_file_path, "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)


def convert_data_to_unicode(data_to_convert):
    for data in data_list:
        if data_to_convert in data["letter"]:
            return data["unicode"]


def convert_data_to_letter(get_data):
    for data in data_list:
        if get_data in data["unicode"]:
            return data["letter"]