import os

                    # DONT GIVE UP




# File zapper should ask for your prefered extension type
inp = raw_input('please choose a directory to search ')
count = 0
rec = raw_input('please choose an extension type ')
# File zapper should then return the number of files
# with that extension type.
for root, dirs, files in os.walk(inp, topdown=True):
    for filename in files:
        if filename.endswith(rec):
            count += 1
print 'you have %d files with the %s extension' % (count, rec)

# filezapper should then present to you further options like
# files returned with size or amount of lines etc etc
choice = raw_input('Would you like to see the file sizes: [y]es, [n]o ')
if choice.lower() == 'y':
    for root, dirs, files in os.walk(inp, topdown=True):
        for filename in files:
            if filename.endswith(rec):
                thefile = os.path.join(root, filename)
                print os.path.getsize(thefile), thefile
                filerange = raw_input('please choose a file size range to continue')
                pass
elif choice.lower() == 'n':
    raw_input





# filezapper should then compile a list of filtered files
# regarding your opption choices


# last you will be asked if you would like to continue with the
# truncation of said files and thats all she wrote
