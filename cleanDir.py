import os
import glob

# Specify the directory you want to clean up
dir = 'output'

# Check if the directory exists
if os.path.exists(dir):
    # Use glob to match all files in the directory
    files = glob.glob(f'{dir}/*')

    # Iterate over the list of filepaths & remove each file.
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print("Error: %s : %s" % (file, e.strerror))
else:
    print(f"The directory {dir} does not exist.")