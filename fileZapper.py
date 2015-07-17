import os
import sys
import re


count = 0
                    #DONT GIVE UP!!!
#find a module to go through my files
for root, dirs, files in os.walk('/Users/', topdown=True):
    for file in files:
        if file.endswith('.torrent'):
           count += 1
           print os.path.join(root, file)

print 'your torrent file count is', count


#find another module to check the extensions on the files


#Write code that removes all files with supplied extension


#Last but not least refine and remaster program


