import models_converter as mc
import os

def convert_files():
    # Create a list of files to be converted
    files = os.listdir('filtered')
    # Iterate over the list of files
    for file in files:
        # Get the full path of the file
        src = os.path.join('filtered', file)
        # Get the filename without the extension
        filename = os.path.splitext(file)[0]
        # Get the full path of the destination file
        dest = os.path.join('converted', filename + '.stl')
        # Convert the file
        mc.file_converter(src, dest)
        print('Converted: ' + file)
            
convert_files()