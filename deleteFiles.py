import os
import time
import shutil

def deleteFiles():
    path = input("Enter Path Name :- ")
    if(os.path.exists(path)):
        getTime = time.time()
        getFilesAndFolders = []
        for (root,dirs,files) in os.walk(path):
            getFilesAndFolders = files + dirs
            for item in getFilesAndFolders:
                itemPath = os.path.join(root, item)
                ctime = os.stat(itemPath).st_ctime
                difference = getTime - ctime
                if difference / (60 * 60 * 24) > 30:
                    name,ext = os.path.splitext(item)
                    path = os.path.join(root,item)
                    if ext == '':
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    print("Items deleted successfully")

deleteFiles()