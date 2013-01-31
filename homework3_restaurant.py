###############################################
# COMS3101.003 - Python - Homework 3
#

################################################
# Part1 - Classes, Methods, Attributes, Instances
#
# Create a module 'restaurant' which contains the following classes:
# (a) Create a class Guest that represents a hungry guest at a restaurant.
# (b) Create a class Restaurant with base class list.
#     Each element in a Restaurant represents a table.
# (c) Create a class FancyRestaurant with base class Restaurant,
#     which overloads the serve(self) method and fixes the problem of (b).

import sys

class Guest(object):

    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def eat(self):
        if(self.hunger != 0):
           self.hunger -= 1 

        if(self.hunger == 0):
            sys.stdout.write("%s: Burp!\n" % self.name)

        return self.hunger

class Restaurant(list):

    def __init__(self, size):
        self.size = size
        self += [None]*size
        
    def seat(self, guest):
        for i in range(len(self)):
            if self[i] == None:
                self[i] = guest
                sys.stdout.write("Seating guest %s at table %d.\n" %\
                                 (guest.name, i))
                return True
        sys.stdout.write("No free table.\n");

    def serve(self):
        for i in range(len(self)):
            if self[i] != None:
                sys.stdout.write("Serving guest %s.\n" % self[i].name)
                hunger = self[i].eat()
                if not hunger:
                    self[i] = None
                return;
        sys.stdout.write("No guest to serve.\n");

class FancyRestaurant(Restaurant):
    
    def __init__(self, size):
        Restaurant.__init__(self, size)
        self.wait = 0 # add a new parameter

    def serve(self):
        for j in range(len(self)):
            i = (self.wait + j) % len(self)
            if self[i] != None:
                sys.stdout.write("Serving guest %s.\n" % self[i].name)
                self.wait = (i+1) % len(self)
                hunger = self[i].eat()
                if not hunger:
                    self[i] = None
                return;
        sys.stdout.write("No guest to serve.\n");


def test1(cls):
    g1 = Guest("Alice",1)
    g2 = Guest("John",2)
    g3 = Guest("Mary",3)

    guests = [g1, g2, g3]

    r = cls(2)
    
    while guests: 
        if r.seat(guests[-1]):
            guests.pop()
        r.serve()

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part1 - Classes, Methods, Attributes, Instances'
    print '#--------------------------------------'
    
    print '\n# test Restaurant : \n'
    test1(Restaurant)
    print '\n# test FancyRestaurant : \n'
    test1(FancyRestaurant)

################################################
# Part2 - Overloading Special Methods
#
# (a) Create a module 'gestures' that defines three classes:
#     Rock, Scissors, and Paper.
#     Make all Rock, Scissors, and Paper instances comparable
#     by overloading the classes' __cmp__(self, other) methods.
# 
# (b) Create a class Player, with a method play(self) that returns
#     an instance object of either Rock, Paper, or Scissors.
#     Your method can randomly select one of the gestures.
#
# (c) Implement a class HumanPlayer with base Player, that overloads 
#     play(self) to read in the user's choice of a gesture from the 
#     keyboard instead of randomly selecting a move.
#
# (d) Write a main function that creates a HumanPlayer and a computer
#    Player, repeatedly requests a gesture from each player instance,
#    compares the result and keeps track of the score. The score and
#    chosen gestures should be printed after each turn
    
import random

class Rock:

    def __str__(self):
        return "Rock"
    
    def __cmp__(self, other):
        if isinstance(other, Rock): return 0
        elif isinstance(other, Scissors): return 1
        elif isinstance(other, Paper): return -1
        else: raise Exception('unknown type')

class Scissors:

    def __str__(self):
        return "Scissors"
    
    def __cmp__(self, other):
        if isinstance(other, Rock): return -1
        elif isinstance(other, Scissors): return 0
        elif isinstance(other, Paper): return 1
        else: raise Exception('unknown type')

class Paper:

    def __str__(self):
        return "Paper"
    
    def __cmp__(self, other):
        if isinstance(other, Rock): return 1
        elif isinstance(other, Scissors): return -1
        elif isinstance(other, Paper): return 0


class Player:
    
    def play(self):
        return random.choice([Rock(), Scissors(), Paper()])

class HumanPlayer(Player):
    
    def play(self):
        while True:
            user = raw_input('Choice a gesture (1:Rock, 2:Scissors, 3:Paper): ')
            if user == "1": return Rock()
            elif user == "2": return Scissors()
            elif user == "3": return Paper()
            else: print 'unknown input!'


def main():
    score = {"human":0, "computer":0}
    time = 10 # play time
    while time != 0:
        computer = Player().play()
        human = HumanPlayer().play()
        if(human < computer):
            winer = "Computer Win!"
            score["computer"] += 1
        elif(human > computer):
            winer = "Human Win!"
            score["human"] += 1
        else:
            winer = "Draw!"
            
        print "Human (%s) vs Comuter (%s) - %s" % (human, computer, winer)
        print "Score: Human(%d) : Computer(%d)\n" % (score["human"], score["computer"])
        time -= 1


if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part2 - Overloading Special Methods'
    print '#--------------------------------------'

    print '\n# test Gesture : \n'
    main()
