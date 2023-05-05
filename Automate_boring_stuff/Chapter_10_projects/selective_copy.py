# Program walks through a folder tree and searches
# for files with a certain file extension (such as .pdf or .jpg).
# Copies these files from whatever location they are into
# a new folder.

import os
import shutil

directory = "C:\\D_Drive\\Python\\"
destination = "C:\\D_Drive\\folder_copy2\\"

for folder_name, sub_folders, filenames in os.walk(directory):
    for filename in filenames:
        file_extension = ".exe"
        if file_extension in filename:
            source_file_path = os.path.join(folder_name, filename)
            dest_file_path = os.path.join(destination, os.path.relpath(source_file_path,directory))
            shutil.copy2(source_file_path, dest_file_path)
            print(F"FILE {filename} COPIED TO {destination}")
