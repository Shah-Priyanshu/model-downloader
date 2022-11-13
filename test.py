import os
import shutil

def filter():
    counter=0
    scounter=0
    for path, subdirs, files in os.walk("unzipped"):
        for name in files:
            #print(os.path.join(path, name))
            counter+=1
            if str(name)[-4:]==".FBX":
                shutil.copy2(os.path.join(path, name),r".\filtered")
                print(os.path.join(path, name))
                scounter+=1
            
    print("total files:",counter)
    print("files copied:",scounter)