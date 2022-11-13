import os
import shutil

def filter(src_dir,dest_dir):
    counter=0
    scounter=0
    for path, subdirs, files in os.walk(src_dir):
        for name in files:
            #print(os.path.join(path, name))
            counter+=1
            if str(name)[-4:]==".FBX":
                shutil.copy2(os.path.join(path, name),dest_dir)
                print(os.path.join(path, name))
                scounter+=1
            
    print("Total files:",counter)
    print("Files copied:",scounter)
    print("Copying completed") 