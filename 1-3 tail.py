#! /usr/bin/env python

# get file name
import sys

if len(sys.argv) != 2:
    filename = "file.txt"
else:
    filename = sys.argv[1]

searchtext = raw_input("Enter search text: ")

print "search text is \"" + searchtext +"\"."
print "file name is \"" + filename + "\"."

#--------------------------------------
# function defination
#--------------------------------------
import time

def tail(f):
    f.seek(0,2) # jump to EOF
    while True:
        line = f.readline() # read line from file
        if not line:    # if no line, sleep a while and try again
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line
    

#--------------------------------------
# unix "tail -f | grep searchtext" in python
#--------------------------------------

logfile = tail(open(filename))
pylines = grep(logfile, searchtext)

for line in pylines:
    print line
