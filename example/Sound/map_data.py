import os
import json


def get_files_in_directory(directory):
    files = []
    # Check if the directory exists
    if os.path.exists(directory):
        # Iterate through all the items in the directory
        for item in os.listdir(directory):
            # Get the full path of the item
            item_path = os.path.join(directory, item)
            # Check if the item is a file
            if os.path.isfile(item_path):
                files.append(item)
    else:
        print("Directory not found.")
    return files


def rename_files_based_on_nepali_order(directory):
    # Get all files in the directory
    files = get_files_in_directory(directory)

    # Sort files based on Nepali order
    files.sort(key=lambda x: ''.join([chr(ord(ch)+2400) for ch in x]))

    # Rename files and store the mapping in a dictionary
    mapping = {}
    for i, file_name in enumerate(files):
        old_path = os.path.join(directory, file_name)
        new_file_name = f"{i+1}.wav"  # Prepend the index
        new_path = os.path.join(directory, new_file_name)
        os.rename(old_path, new_path)
        mapping[file_name] = new_file_name
        print(f"Renamed '{file_name}' to '{new_file_name}'")

    # Write the mapping to a JSON file
    with open(os.path.join(directory, 'file_mapping.json'), 'w') as json_file:
        json.dump(mapping, json_file, indent=4)
    print("Mapping stored in 'file_mapping.json'.")


# Example usage
directory_path = 'example\Sound\consonant'
rename_files_based_on_nepali_order(directory_path)
