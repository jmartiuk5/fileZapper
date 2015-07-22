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
#TODO Add this logic to program to do the removing
# if size == 2578 or size == 2565:
    # print 'T-Mobile:',thefile
    # os.remove(thefile)
    # continue

# if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
#     print 'iPhone:', thefile
#     os.remove(thefile)
#     continue
#
#Last but not least refine and remaster program


