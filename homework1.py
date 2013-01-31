###############################################
# COMS3101.003 - Python - Homework 1
#
# Please fill in your solutions for part 2 to 5 
# below. 

################################################
# Part 1 - Control Flow
#
# Implement a simple guessing game.
# The program chooses a secret number x between 1 and 10.
# The player can guess numbers repeatedly.
# After each guess, the program prints a hint.
# * if the difference between x and the guess is greater than 5,
#   the program prints 'not even close'.
# * if the difference between x and the guess is between 3 and 5,
#   the program prints 'close'.
# * if the difference between x and the guess is less than 3,
#   the program prints 'almost there'.
# If the player guesses x correctly, the program prints a message and terminates.
# The program keeps track of the number of guesses.
# If the user cannot guess x in his fifth guess,
# the program informs him that the game is lost and terminates.

import random

print '#--------------------------------------'
print '# Part 1 - Control Flow'
print '#--------------------------------------'

def guessing():
    """ Implement a simple guessing game.
        The program chooses a secret number x between 1 and 10.
        The player can guess numbers repeatedly.
        After each guess, the program prints a hint."""
    secret_number = random.choice(range(1,11))
    guess_time = 0;

    while True:
        try:
            guess = int(raw_input('Guess a number between 1 and 10: '))
        except Exception as e:
            print e
            return;
        else:
            if(guess == secret_number):
                print "you got it, %d is the secret number!" % guess
                return;
            elif (abs(guess - secret_number) > 5):
                print "not even close..."
            elif (abs(guess - secret_number) >= 3):
                print "close..."
            else:
                print "almost there!"
                
            guess_time += 1
            if(guess_time == 5):
                print "the game is lost..."
                return
            
# test the program        
guessing()

################################################
# Part 2 - Lists and for-Loops
#
# Use two nested for loops to compute the value 
# of expressions of the form 
# (a[1]+...+a[m])*(b[1]+...+b[m]).
# 
# Assume that a and b are arbitrary sequences of numbers.
# For instance, for a = [1, 2, 4] and b = [2, 3] the result would be 35.

print '#--------------------------------------'
print '# Part 2 - Lists and for-Loops'
print '#--------------------------------------'

a = [1, 2, 4]
b = [2, 3]

#Your code starts here

def sum_product(a,b):
    """ Use two nested for loops to compute the valueof expressions
        of the form:
        (a[1] + a[2] + ... + a[m]) * (b[1] + b[2] + ... + b[n])
        Assume that a and b are arbitrary sequences of numbers.
        PS. Equal to: sum(a) * sum(b)"""
    sum = 0
    for i in a:
        for j in b:
            sum += i*j

    return sum

# get the result of sum(a) * sum(b)
print a, "*", b, "=", sum_product(a,b)

#Your code ends here


#################################################
# Part 3 - List Comprehension
#
# Given a sequence lst, using a list comprehension create a list that is 
# identical to lst, but without elements that have an identical element next
# to them. For instance the, list
#         lst = ['a','b','b','c','a','a','b','c','a','a']
# should produce the answer ['a','c','b','c'].
#
# Pay attention to the first and last element. 
# Instead of iterating over elements of l, you should iterate over indices 
# of lst. This should work for arbitrary sequences of arbitary length.

print '#--------------------------------------'
print '# Part 3 - List Comprehension'
print '#--------------------------------------'

lst= list('abbcaabcaa')

#Your code starts here

new_lst = [lst[i] for i in range(len(lst)) if \
           (i==0 or lst[i-1]!=lst[i]) and \
           (i==len(lst)-1 or lst[i+1]!=lst[i])]

print lst, "->", new_lst

#Your code ends here


#################################################
# Part 4 - List Comprehension
#
# Assume we have the following dictionary:
# fruit_to_color = {'banana':'yellow',
#                  'blueberry':'blue',
#                  'cherry':'red',
#                  'lemon':'yellow',
#                  'kiwi':'green',
#                  'strawberry':'red',
#                  'tomato':'red'}
#
# Write a program that creates a dictionary that maps colors to lists of
# fruits that have this color, e.g. color_to_fruits['yellow'] should produce
# ['banana','lemon'].
#
# Hint: Before you can add an item to a list it has to be initialize. This 
# has to be done the first time you add any fruit of a color (i.e. when color
# to fruits does not yet have a key for this color).

print '#--------------------------------------'
print '# Part 4 - List Comprehension'
print '#--------------------------------------'

fruit_to_color = {'banana':'yellow',
                  'blueberry':'blue',
                  'cherry':'red',
                  'lemon':'yellow',
                  'kiwi':'green',
                  'strawberry':'red',
                  'tomato':'red'}
#Your code starts here

def reverseDict(d):
    """ Given a dictionary, creates a dictionary
        that maps values to lists of keys. """
    r = {}
    for value in d.values():
        r[value] = []
    for key in d.keys():
        r[d[key]].append(key)
    return r

color_to_fruit = reverseDict(fruit_to_color)
print fruit_to_color
print color_to_fruit

#Your code ends here


#################################################
# Part 5 - Dictionary Comprehension
#
# Dictionary comprehensions can create dictionaries from sequence in much the
# same way that list comprehensions create lists. They are a new feature in
# Python 2.7 and 3.x.
#
# The basic syntax is:
#      {key expression : value expression for x in sequence if condition}
#
# Given the following list of words, use a dictionary comprehension to build
# a dictionary that maps each word to its length.

print '#--------------------------------------'
print '# Part 5 - Dictionary Comprehension'
print '#--------------------------------------'

words = ['you','must','return','here','with','a','shrubbery','or','else']

#Your code starts here

print {x:len(x) for x in words}

#Your code ends here
