#!/usr/bin/env python

#Here, you have to use multiprocessing and subprocess module methods to sync the data from /data/prod to /data/prod_backup folder.

#Hint: os.walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up. This is used to traverse the file system in Python. 

import subprocess
src = "/data/prod/"
dest = "/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
