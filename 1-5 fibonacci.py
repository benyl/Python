#! /usr/bin/env python

# fibonacci function: fib[n] = fib[n-1] + fib[n-2]

#--------------------------------------
# version 1: use return
#--------------------------------------
def fib1(max):
    a, b, i = 0, 1, 0
    while i<max:
        a, b, i = b, a + b, i+1
        #print 'fib(%d) = %d' % (i,a)
    return a
    
#--------------------------------------
print 'fib1(%d) = %d' % (10,fib1(10))


#--------------------------------------
# version 2: use yield
#--------------------------------------
def fib2(max):
    a, b = 0, 1
    for _ in xrange(max):
        a, b = b, a + b
        yield a
    
#--------------------------------------
b = fib2(10)
for i in range(10):
    print b.next(),

print '\nfib2(10) =', list(fib2(10)) # another option


#--------------------------------------
# version 3: use iterable class
#--------------------------------------
class fib3(object):

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()

#--------------------------------------
for i in fib3(10):
    print i,

print '\nfib3(10) =', list(fib3(10))


#--------------------------------------
from inspect import isgeneratorfunction
print isgeneratorfunction(fib1), \
      isgeneratorfunction(fib2), \
      isgeneratorfunction(fib3)

import types
print isinstance(fib2, types.GeneratorType), \
      isinstance(fib2(10), types.GeneratorType)


from collections import Iterable
print isinstance(fib2, Iterable) , \
      isinstance(fib2(10), Iterable) 

