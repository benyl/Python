###############################################
# COMS3101.003 - Python - Homework 5
#

################################################
# Part 1 - schoenfinkeled decorator
#
# Write a function decorator that allows to schoenfinkeled a function.
# schoenfinkeled is a transformation that modies a function with n
# parameters so that it can be called as a chain of n functions each
# taking a single parameter.

def schoenfinkeled(func):
    
    def deco(*args):
        if(len(args) != 1):
            raise TypeError(\
                '%s takes exactly 1 argument (%d given)'\
                %(fun.__name__, len(args)))

        argstr = ','.join([repr(arg) for arg in args])
        print "calling %s(%s)" % (func.__name__, argstr)
        
        try:
            return func(*args)
        except Exception:
            @schoenfinkeled
            def newfunc(*args2):
                return func(*args + args2)
            return newfunc
        
    return deco

@schoenfinkeled
def add(a,b,c):
    return a + b + c

def test1():
    print add(1)(2)(3)

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 1 - schoenfinkeled decorator'
    print '#--------------------------------------'
    test1()

################################################
# Part 2 - Crawling the Web with Regular Expressions
#
# Write a program that accepts a start web address and a recursion depth
# d as command line arguments. The program should read in the web
# document at the start address, extract all web links that are 
# mentioned in the document using regular expressions, and then continue
# the process recursively for each link until d recursion levels have 
# been reached. If the program is called with recursion depth 0, only
# the document at the start address should be retrieved.

import urllib2, re

def matchurl(url):
    url_re = re.compile("<a href=[ ]*[\"\']http://[^\"^\']*[\"\']>")
    ignore = [".pdf", ".txt", ".jpg", ".png"]

    url_lst = []
    for line in urllib2.urlopen(url):
        match = url_re.search(line.lower())
        if match:
            url_str = line[match.start()+9:match.end()-2]
            
            if url_str.endswith("/"):
                url_str = url_str[:-1]
                
            for word in ignore:
                if url_str.endswith(word):
                    url_str = []
                    break;

            if url_str:
                url_lst.append(url_str)

    return url_lst

def crawler(start_url, depth):
    
    url_level = [[start_url]]
    url_add = [start_url]

    for i in xrange(depth-1):
        url_lst = []
        url_level.append([])
        
        for j in xrange(len(url_level[i])):
            url = url_level[i][j]
            try:
                url_lst += matchurl(url)
            except urllib2.URLError:
                print "Error:", url_level[i][j], "CANNOT OPEN!"
                
        for url in url_lst:
            if url not in url_add:
                url_level[i+1].append(url)
                url_add.append(url)
                
    return url_level

def test2():
    start_url = "http://www.cs.columbia.edu/~bauer/cs3101-3" # start url
    depth = 3

    url_level = crawler(start_url, depth)

    for i in xrange(len(url_level)):
        for j in xrange(len(url_level[i])):
            pre = "- " * i
            print pre + url_level[i][j]

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 2 - Crawling the Web with Regular Expressions'
    print '#--------------------------------------'
    test2()

################################################
# Part 3 - Rock, Paper, Scissors Revisited
#
# (a) Create a new class AiPlayer that uses Player as a base class.
#     Add a new method learn(gesture) to Player which is used to
#     communicate an opponents last gesture.

import random
from homework3_restaurant import *

class AiPlayer(Player):

    def __init__(self):
        self.gest1 = None
        self.gest2 = None
        
        self.record = {}

        gestures = ["Rock", "Scissors", "Paper"]
        for i in gestures:
            for j in gestures:
                self.record[(i,j)] = {}
                for k in gestures:
                    self.record[(i,j)][k] = 0
        
        return
    
    def play(self):
        if self.gest1 and self.gest2:
            key,_ = max(self.record[(self.gest1,self.gest2)]\
                            .iteritems(), key=lambda x:x[1])
            
            if key == "Rock": return Paper()
            elif key == "Scissors": return Rock()
            elif key == "Paper": return Scissors()
        else:    
            return random.choice([Rock(), Scissors(), Paper()])

    def learn(self, gestures):
        gest = str(gestures)
        
        if self.gest1 and self.gest2:
            self.record[(self.gest1,self.gest2)][gest] += 1
            
        self.gest1 = self.gest2
        self.gest2 = gest
        
        return

def test3():
    score = {"human":0, "computer":0}
    time = 20 # play time
    com = AiPlayer()
    hum = HumanPlayer()
    while time != 0:
        com_gest = com.play()
        hum_gest = hum.play()
        if(hum_gest < com_gest):
            winer = "Computer Win!"
            score["computer"] += 1
        elif(hum_gest > com_gest):
            winer = "Human Win!"
            score["human"] += 1
        else:
            winer = "Draw!"

        #print "Human (%s) vs Comuter (%s) - %s" % (hum_gest, com_gest, winer)
        #print "Score: Human(%d) : Computer(%d)" % (score["human"], score["computer"])

        print "%s vs %s - %s - (%d:%d)" % \
              (hum_gest, com_gest, winer,score["human"], score["computer"])
        com.learn(hum_gest)

        time -= 1


if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 3 - Rock, Paper, Scissors Revisited'
    print '#--------------------------------------'
    test3()

