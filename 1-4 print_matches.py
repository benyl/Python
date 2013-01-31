#! /usr/bin/env python

# example about yield

def print_matches(matchtext):
    print "Looking for", matchtext
    while True:
        line = (yield) # get a line of text
        if matchtext in line:
            print line

print """>>> matcher = print_matches("python")"""
matcher = print_matches("python")

print """>>> matcher.next()"""
matcher.next()

print """>>> matcher.send("Hello World")"""
matcher.send("Hello World")

print """>>> matcher.send("python is cool")"""
matcher.send("python is cool")

print """>>> matcher.send("good bye")"""
matcher.send("good bye")

print """>>> matcher.close()"""
matcher.close()
