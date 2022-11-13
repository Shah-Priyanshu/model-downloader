import os

def create(): # create folders
    folder_downloaded = "downloaded" # folder name
    folder_unzipped = "unzipped" # folder name
    folder_filtered = "filtered" # folder name
    folder_converted = "converted" # folder name

    parent_directory= "./" # parent directory
    path1=os.path.join(parent_directory,folder_downloaded) # path to folder
    path2=os.path.join(parent_directory,folder_unzipped) # path to folder
    path3=os.path.join(parent_directory,folder_filtered) # path to folder
    path4=os.path.join(parent_directory,folder_converted) # path to folder

    os.makedirs(path1, exist_ok=True) # create folder if it doesn't exist
    os.makedirs(path2, exist_ok=True) # create folder if it doesn't exist
    os.makedirs(path3, exist_ok=True) # create folder if it doesn't exist
    os.makedirs(path4, exist_ok=True) # create folder if it doesn't exist