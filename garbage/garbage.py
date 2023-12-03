from urllib import request
import os
import zipfile
import tempfile  # Import the tempfile module

def get_path_dataset():

# Create a temporary directory for storing the ZIP file
    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
# Define the default and backup server URLs for downloading the dataset
    default_server_url = "http://clouds.iec-uit.com/smartbin.test1/Dataset.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GYBKU365PB7L3NP1SEUR%2F20231203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231203T114849Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJHWUJLVTM2NVBCN0wzTlAxU0VVUiIsImV4cCI6MTcwMTY0NzI4MiwicGFyZW50Ijoic21hcnRiaW4ifQ.EAxA8gkGhQSc1ONiTCXJujJcROMPgNdtxeDZnADEtZ7C_p209rBAA1J5CPUVhWZS6Em7fQdV3koOk21Qa6OWiA&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=0080c1bf45c8399b6fc9e60d000e0efdc9287080951d349134769e7817e76a2e"
    backup_server_url = "http://clouds.iec-uit.com/smartbin.test1/Dataset.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GYBKU365PB7L3NP1SEUR%2F20231203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231203T114849Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJHWUJLVTM2NVBCN0wzTlAxU0VVUiIsImV4cCI6MTcwMTY0NzI4MiwicGFyZW50Ijoic21hcnRiaW4ifQ.EAxA8gkGhQSc1ONiTCXJujJcROMPgNdtxeDZnADEtZ7C_p209rBAA1J5CPUVhWZS6Em7fQdV3koOk21Qa6OWiA&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=0080c1bf45c8399b6fc9e60d000e0efdc9287080951d349134769e7817e76a2e"
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