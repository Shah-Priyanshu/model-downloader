import requests
import time
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool   
import time       

def download_url(input): # download files
    t0 = time.time() # start time
    url, fn = input[0], input[1] # get url and filename
    try: # try to download file
        r = requests.get(url) # get request
        with open(fn, 'wb') as f: # open file in write mode
            f.write(r.content) # write content to file
            time.sleep(3)
        return(url, time.time() - t0) # return url and time taken
    except Exception as e: # if error
        print('Exception in download_url():', e) # print error
        
def downloads(input): # download files
    counter=0 # initialize counter
    cpus = cpu_count() # get number of cpus
    results = ThreadPool(cpus - 1).imap_unordered(download_url, input) # download files
    for result in results: # iterate over results
        print('url:', result[0], 'time (s):', result[1]) # print url and time taken
        counter+=1 # increment counter
    print("Download complete") # print message
    print(counter, 'files downloaded') # print number of files downloaded