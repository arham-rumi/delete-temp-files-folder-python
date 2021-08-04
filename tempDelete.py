# Program to Delete all the files in the temp folder
# Reference: https://realpython.com/working-with-files-in-python/

# Importing some modules / Libraries
from pathlib import Path
import platform
import os
import shutil
import tempfile

# Getting the Temp directory
temp_path = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())

# Initiallizing the deleting counters
deleted_files = deleted_folders = 0

# Listing up files
for current_file in os.listdir(temp_path):
    complete_file_path = os.path.join(temp_path, current_file)
    back_slash_index = complete_file_path.find('\\')
    file_name = complete_file_path[back_slash_index + 1:]

    # Deleting the Files / Folders
    # It up to you to use remove / unlink methods
    try:

        # Deleting the Files
        if os.path.isfile(complete_file_path):
            os.remove(complete_file_path)
            print(f"{file_name} is deleted" )
            deleted_files += 1
        
        # Deleting the Folders
        elif os.path.isdir(complete_file_path):
            if complete_file_path.__contains__('chocolatey'):
                continue
            shutil.rmtree(complete_file_path)
            print(f"{file_name} is deleted" )
            deleted_folders += 1

    except Exception as e:
        print(f"Failed to delete : {file_name}" )

print(f" {deleted_files} files and {deleted_folders} folders are successfully DELETED")