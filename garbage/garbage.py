from urllib import request
import os
import zipfile
import tempfile  # Import the tempfile module

def get_path_dataset():

# Create a temporary directory for storing the ZIP file
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
# Define the default and backup server URLs for downloading the dataset
    default_server_url = "https://drive.google.com/file/d/1xWblKHCgsMPm60IwdNN8vVTIL3T1PdZj/view?usp=sharing"
    backup_server_url = "https://drive.google.com/file/d/1xWblKHCgsMPm60IwdNN8vVTIL3T1PdZj/view?usp=sharing"
# Specify the path for the downloaded ZIP file in the temporary directory
    zip_file_path = os.path.join(temp_dir, "dataset.zip")
    print("zip_file_path", zip_file_path)
# Check if the ZIP file already exists, if not, attempt to download it
    if not os.path.exists(zip_file_path):
        try:
# Try to download from the default server URL
            request.urlretrieve(default_server_url, zip_file_path)
            print("download succeesfully1")
        except:
            request.urlretrieve(backup_server_url, zip_file_path)
            print("download succeesfully")
    return "hi"

def get_list_dataset():
    """
    Get a list of dataset names available in the ZIP archive.

    Returns:
        list: A list of dataset names.
    """
    # Print and return a list of dataset names
    return ['trash', 'shoes', 'plastic', 'paper', 'metal', 'glass', 'clothes', 'cardboard', 'biological', 'battery']