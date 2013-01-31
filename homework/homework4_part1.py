###############################################
# COMS3101.003 - Python - Homework 4
#

################################################
# Part1 - Searching the File System
#
# Use the `os' and `os.path' module to write a Python program
# (`part1.py') that will recursively search through a directory
# hierarchy and print out the absolute paths of all files that have
# a filename related to marijuana. Such a filename contains one of
# the words 'marijuana, marihuana, cannabis, weed' or both the words
# 'mary' and 'jane' together.

import os, sys

def matchfile(filename):
    filename = filename.lower() # Make sure comparisons are case-insensitive
    keyword = ['marijuana', 'marihuana', 'cannabis', 'weed']
    
    for word in keyword:
        if word in filename:
            return True
    else:
        return ('mary' in filename) and ('jane' in filename)

def searchdir(path):
    
    if not os.path.isdir(path):
        print path, "is not dir"
        return

    subdir = []
    filelist = os.listdir(path)
    for f in filelist:
        if os.path.isdir(os.path.join(path,f)):
            subdir.append(f)
        elif os.path.isfile(os.path.join(path,f)):
            if matchfile(f):
                print os.path.join(path,f)

    for f in subdir:
        searchdir(os.path.join(path,f))

def main():
    
    if len(sys.argv) != 2:
        path = os.getcwd() # current directory
        print "no path provided, search current directory:", path
    else:
        path = sys.argv[1]
        print "search path:", path
        
    searchdir(path)


if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 1 - Searching the File System'
    print '#--------------------------------------'
    main()
