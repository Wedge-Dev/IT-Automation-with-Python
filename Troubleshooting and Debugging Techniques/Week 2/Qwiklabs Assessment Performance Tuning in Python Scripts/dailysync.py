#!/usr/bin/env python

#Here, you have to use multiprocessing and subprocess module methods to sync the data from /data/prod to /data/prod_backup folder.
#Hint: os.walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.
#This is used to traverse the file system in Python.

import subprocess
from multiprocessing import Pool
import os

src = "../data/prod/"
dest = "../data/prod_backup/"

def run(dirname) :
    subprocess.call(["rsync", "-arq", src +dirname, dest +dirname])

if __name__ == "__main__" :
    for root, dirs, files in os.walk(src) :
        if len(dirs) > 0 : break
    p = Pool(len(dirs))
    p.map(run, dirs)

### or ###

#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os

src = "../data/prod/"
dest = "../data/prod_backup/"

def run(dirname) :
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__" :
    for root, dirs, files in os.walk(src) :
        if len(files) > 0 : break
    p = Pool(len(files))
    p.map(run, files)
