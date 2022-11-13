import os
import zipfile36 as zipfile
              
def unzip_file(source_dir, dest_dir): # unzip files
    counter=0 # initialize counter
    for file in os.listdir(source_dir): # iterate over files in source directory
        if file.endswith('.zip'): # if file is a zip file
            zip_ref = zipfile.ZipFile(source_dir+file, 'r')  # create zipfile object
            zip_ref.extractall(dest_dir) # extract file to destination directory
            zip_ref.close() # close file
            counter+=1 # increment counter
            print(file, 'unzipped') # print message
    print(counter, 'files extracted') # print number of files extracted
    print('Extraction complete') # print message