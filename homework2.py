###############################################
# COMS3101.003 - Python - Homework 2
#

################################################
# Part 1 - Files and String Processing
#
# (a) Write a function that, given a filename,
#     opens the file in the format described and reads in the data.
# (b) Using Python string formatting, write a function that,
#     given the parameters state, name, address, town, zip,
#     returns a formatted string.
# (c) Write a program that first reads in the data file once
#     (using the function from part (a)),
#     and then asks the user repeatedly to enter a zip code or a town name
#     (in a while loop until the user types "quit").

print '#--------------------------------------'
print '# Part 1 - Files and String Processing'
print '#--------------------------------------'

#--------------------------------------
print '\n# (a) read data from file : \n'

filename = "homework2_markets.tsv"

def read_market(filename):
    zip_map = {}
    town_map = {}
    for line in open(filename):
        (state, name, address, town, zip, longitude, latitude) = \
                line.strip().split("\t")

        # handle error lines
        if zip == "" or town == "": continue;
        if state == "": state = "None"
        if name == "": name = "None"
        if address == "": address = "None"

        fields = (state, name, address, town, zip, longitude, latitude)

        if zip not in zip_map:
            zip_map[zip] = []
        zip_map[zip].append(fields)

        if town.lower() not in town_map:
            town_map[town.lower()] = []

        if zip not in town_map[town.lower()]:
            town_map[town.lower()].append(zip)

    return zip_map, town_map
    
zip_map, town_map = read_market(filename)
print zip_map['36202']
print town_map['Anniston'.lower()]


#--------------------------------------
print '\n# (b) string formatting : \n'

def format_addr(state, name, address, town, zip):
    return "{0}\n{1}\n{2}, {3} {4}".format(name, address, town, state, zip)

state, name, address, town, zip = \
       "New York", "Columbia University Greenmarket", \
       "E. Side of Broadway between 114th & 115th Streets",\
       "New York", "10027"

print format_addr(state, name, address, town, zip)


#--------------------------------------
print '\n# (c) user request : \n'

import sys

def request():
    zip_map, town_map = read_market(filename)

    while True:
        query = raw_input('input a town or zip: ').lower()
        if query == "" or query == "quit" :
            sys.stdout.write("good bye!\n\n")
            break;
        else:
            if query.isdigit() and (query in zip_map):
                for field in zip_map[query]:
                    (state, name, address, town, zip, \
                     longitude, latitude) = field
                    output = format_addr(state, name, address, town, zip) + "\n\n"
                    sys.stdout.write(output)
            elif (not query.isdigit()) and (query in town_map):
                for zips in town_map[query]:
                    for field in zip_map[zips]:
                        (state, name, address, town, zip, \
                         longitude, latitude) = field
                        output = format_addr(state, name, address, town, zip) + "\n\n"
                        sys.stdout.write(output)
            else: sys.stdout.write("no matching marcket!\n\n")
        
request()


################################################
# Part 2 - Generators
#
# Write a generator function called multgen that takes two lists
# of integers of equal length and, on each turn, yields the result
# of multiplying corresponding integers.

print '#--------------------------------------'
print '# Part 2 - Generators'
print '#--------------------------------------'

def multgen(a, b):
    for i in range(len(a)):
        yield a[i]*b[i]

for product in multgen([1,2,3],[1,2,3]):
    print(product)

print ""

################################################
# Problem 3 - First-class Functions and lambda expressions
#
# Modify your multgen function from Problem 2 into a new function
# called genmap, that takes a function object as the first parameter,
# and two equal length lists as the second and third parameters.
# The genmap function should yield the result of applying the first
# parameter to corresponding elements of the two lists on each turn.

print '#--------------------------------------'
print '# Problem 3 - First-class Functions and lambda expressions'
print '#--------------------------------------'

def genmap(x, a, b):
    for i in range(len(a)):
        yield x(a[i], b[i])

def multgen2(a, b):
    for ans in genmap(lambda x,y : x*y, a, b):
        yield ans

print list(genmap(lambda a,b: a*b, [1,2,3],[1,2,3]))
print list(multgen2([1,2,3],[1,2,3]))
