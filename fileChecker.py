import os


for root, dirs, files in os.walk('/Users/', topdown=True):
    for filename in files:
        if filename.endswith('.py'):
            theFile = os.path.join(root, filename)
            size = os.path.getsize(theFile)
            if size > 300:
                continue
            fhand = open(theFile, 'r')
            lines = list()
            for line in fhand:
                lines.append(line)
            fhand.close()
            if len(lines) > 1:
                print len(lines), theFile
                print lines[:4]
