import glob
import os

# Specify the directory you want to clean up
dir_folder = 'output'

# Check if the directory exists
if os.path.exists(dir_folder):
    # Use glob to match all files in the directory
    files = glob.glob(f'{dir_folder}/*')

    # Iterate over the list of filepaths & remove each file.
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print("Error: %s : %s" % (file, e.strerror))
    print(f"Directory {dir_folder} cleaned successfully.")
else:
    print(f"The directory {dir_folder} does not exist.")