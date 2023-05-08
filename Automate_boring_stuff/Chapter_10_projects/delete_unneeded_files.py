# Program walks through a folder tree and looks for files with
# size over 100mb and prints out its path (or deletes it)
import os


def print_large_files(start_path):
    for foldername, subfolders, filenames in os.walk(start_path):
        for file in filenames:
            file_path = os.path.join(foldername, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) > 100 * 1024 * 1024:
                print("File:", file_path)
        for subfolder in subfolders:
            subfolder_path = os.path.join(foldername, subfolder)
            if os.path.isdir(subfolder_path):
                folder_size = get_folder_size(subfolder_path)
                if folder_size > 100 * 1024 * 1024:
                    print("Folder:", subfolder_path)


def get_folder_size(folder):
    total_size = 0
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


source_directory = "C:\\D_Drive\\"
print_large_files(source_directory)
