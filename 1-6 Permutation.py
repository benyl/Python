#! /usr/bin/env python

# Permutation: return all combination of the elements in a list

#--------------------------------------
# version 1: use recursion
#--------------------------------------
def permute(inputData, outputSoFar):
    for elem in inputData:
        if elem not in outputSoFar:
            outputSoFar.append(elem)
            if len(outputSoFar) == len(inputData):
                print outputSoFar
            else:
                permute(inputData, outputSoFar)  # --- Recursion
            outputSoFar.pop()

print "version 1: use recursion"
permute([1, 2, 3], [])

#--------------------------------------
# version 2: use class
#--------------------------------------
class Permutation:
    def __init__(self, justalist):
        self._data = justalist[:]
        self._sofar = []

    def __iter__(self):
        return self.next()

    def next(self):
        for elem in self._data:
            if elem not in self._sofar:
                self._sofar.append(elem)
                if len(self._sofar) == len(self._data):
                    yield self._sofar[:]
                else:
                    for v in self.next(): # use a loop of yeild here
                        yield v           # to return the result to 'top layer'
                self._sofar.pop()
                
print "version 2: use class"
for i in Permutation([1,2,3]):
    print i

#--------------------------------------
# version 3: better solution in itertools
#--------------------------------------
import itertools

##def permutations(iterable, r=None):
##    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
##    # permutations(range(3)) --> 012 021 102 120 201 210
##    pool = tuple(iterable)
##    n = len(pool)
##    r = n if r is None else r
##    if r > n:
##        return
##    indices = range(n)
##    cycles = range(n, n-r, -1)
##    yield tuple(pool[i] for i in indices[:r])
##    while n:
##        for i in reversed(range(r)):
##            cycles[i] -= 1
##            if cycles[i] == 0:
##                indices[i:] = indices[i+1:] + indices[i:i+1]
##                cycles[i] = n - i
##            else:
##                j = cycles[i]
##                indices[i], indices[-j] = indices[-j], indices[i]
##                yield tuple(pool[i] for i in indices[:r])
##                break
##        else:
##            return

print "version 3: using itertools"
for i in itertools.permutations ([1,2,3]):
    print i

#--------------------------------------
# version 4: use product function in itertools
#--------------------------------------

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutation_pro(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

print "version 4: use product function"
for i in permutation_pro ([1,2,3]):
    print i
