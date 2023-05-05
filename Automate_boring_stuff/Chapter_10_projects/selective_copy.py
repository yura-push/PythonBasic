# Program walks through a folder tree and searches
# for files with a certain file extension (such as .pdf or .jpg).
# Copies these files from whatever location they are into
# a new folder.

import os
import shutil

directory = "C:\\D_Drive\\Python\\"
destination = "C:\\D_Drive\\folder_copy2\\"

for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".exe"):
            source_file_path = os.path.join(foldername, filename)
            dest_file_path = os.path.join(destination, os.path.relpath(source_file_path, directory))
            # Checks if all directories exist in destination
            # if not, creates folders and copies files.
            if not os.path.exists(dest_file_path):
                os.makedirs(dest_file_path)
                shutil.copy2(source_file_path, dest_file_path)
                print(F"FILE {filename} COPIED FROM {foldername} TO {dest_file_path}")
