from folder_creator import create
from download import downloads
from unzip import unzip_file
from file_filter import filter
#from file_converter import converter

def main():
    create() # create folders
    
    file = open('urls.txt', 'r') # open file in read mode
    url=[] # create empty list
    for line in file: # iterate over each line in file
        line = line.strip('\n') # remove '\n' from each line
        url.append(line) # append each line to list
    fns = ['downloaded\\file' + str(i) + '.zip' for i in range(1,len(url)+1)] # create list of filenames
    input=zip(url,fns) # create list of tuples
    #downloads(input) # download files
    
    source= 'downloaded\\'  # source directory
    dest= 'unzipped\\' # destination directory
    #unzip_file(source,dest) # unzip files
    
    filter_source= 'unzipped' # source directory
    filter_dest= 'filtered' # destination directory
    #filter(filter_source, filter_dest) # filter files

    src= r'L:\Projects\Model-Downloader\filtered\Abra.FBX' # source directory
    dest= r'L:\Projects\Model-Downloader\converted\Abra.stl' # destination directory
    #converter(src,dest) # convert files

# Call the main function
main()    