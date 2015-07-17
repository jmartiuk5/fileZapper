import os
from os.path import join


for dirname, dirs, files in os.walk('/Users/', topdown=True):
    for filename in files:
        if filename.endswith('.torrent'):
            theFile = os.path.join(dirname, filename)
            print os.path.getsize(theFile), theFile


