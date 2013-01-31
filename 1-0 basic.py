#! /usr/bin/env python

import sys
print sys.version

#--------------------------------------
# basic python
#--------------------------------------

print '#--------------------------------------'
print '# int / double / string / boolean'
print '#--------------------------------------'
temp = 1
print temp

temp = 1.0
print temp

temp = "hello world"
print temp

temp = True
print temp 

print '#--------------------------------------'
print '# if else'
print '#--------------------------------------'
temp  = "hello"
if temp > "world":
    print temp, "> world"
elif temp > "hell":
    print temp, "> hell"
else:
    print temp, "<= hell"

print '#--------------------------------------'
print '# while loop'
print '#--------------------------------------'
principal = 1000
rate = 0.05
year = 10
i = 1
print "year =", year, ", principal =", principal, ", rate =", rate

while i <= year:
    principal *= 1 + rate
    print 'year[%2d]=%.2f'%(i, principal)
    i += 1

print '\nwhile1: ',
x = 5
while x:
    print x,
    x-=1

print '\nwhile2: ',
x = 5
while True:
    print x,
    x-=1
    if x==0:
        break

print '\nfor1: ',
for x in xrange(5,0,-1):
    print x,

print '\nfor2: ',
for x in xrange(5,0,-1):
    if x % 2 == 0:
        continue
    print x,

print ""


print '#--------------------------------------'
print '# file'
print '#--------------------------------------'
for line in open("file.txt"):
    print line,
print ""

print '#--------------------------------------'
print '# string'
print '#--------------------------------------'
s1 = "hello world"
s2 = 'good morning'
s3 = """h
a
p
p
y"""
print s1, s2, s3
print s1[0], s2[0], s3[0]
print s1[:5]
print s1[5:]
print s1[3:8]

s1="12"
s2="34"
print s1 + s2, 'len:', len(s1+s2)
print int(s1) + int(s2)
print float(s1) + float(s2)

s1 = 12
s2 = 34
print s1 + s2
print str(s1) + str(s2)
print format(s1,"4d") + format(s2,"04d")

s1 = 'banana'
s2 = 'a'
print s1.count(s2), s1.index(s2)

s1 = "hello world"
s2 = "war"
s3 = "in" if (s2 in s1) else "not in"
print s2, "is", s3, s1

print '#--------------------------------------'
print '# list'
print '#--------------------------------------'
name = ['tom','biz','bob','sue','may']
name.insert(1, 'ivy')
name += [['ray','zoo']]
print 'name =', name,'len =',len(name)
a = name[4:] # = [name[4], name[5], name[6]]
print a
print name[6][0]
print name[3], name.index('bob')
name[0] = 'joe'
print max(name)

print name.pop()
print name
name.remove('biz')
print name
name.reverse()
print name
name.sort()
print name

print xrange(10)
print range(10)

print [x**2 for x in xrange(10) if x%2 !=0]
print [x**2 if x%2 !=0 else "null" \
       for x in xrange(10)]
print [(x,y) for x in xrange(5) if x%2 == 0 \
       for y in "abc" if y!='b']

print '#--------------------------------------'
print '# tuple'
print '#--------------------------------------'
name = ('tom','biz','bob','sue','may')
name += (('ray','zoo'))
print name

print '#--------------------------------------'
print '# set'
print '#--------------------------------------'
name = ['tom','tom','sue']
print set(name)
s1 = [1,2,3,4]
s2 = [3,4,5,6]
print set(s1) | set(s2)
print set(s1) & set(s2)
print set(s1) - set(s2)
print (set(s1) | set(s2)) - (set(s1) & set(s2))


print '#--------------------------------------'
print '# dict'
print '#--------------------------------------'
phone = {'bob':123456, 'tom':"1-1-9", 'ray':[800,100,100]}
print phone["ray"]
phone['joe']="1-XXX-ABC"
phone.pop('ray')
print phone
print phone.keys()
print phone.values()
print phone.items()


import random
newdict = {chr(k):random.randint(0,100) for k in xrange(ord('A'),ord('Z'))}
print newdict
key,value = max(newdict.iteritems(), key=lambda x:x[1])
print key,value

music = [
    {'name': 'Django Reinhardt', 'genre': 'jazz'},
    {'name': 'Jimi Hendrix',     'genre': 'rock'},
    {'name': 'Louis Armstrong',  'genre': 'jazz'},
    {'name': 'Pete Townsend',    'genre': 'rock'},
    {'name': 'Yanni',            'genre': 'new age'},
    {'name': 'Ella Fitzgerald',  'genre': 'jazz'},
    {'name': 'Wesley Willis',    'genre': 'casio'},
    {'name': 'John Lennon',      'genre': 'rock'},
    {'name': 'Bono',             'genre': 'rock'},
    {'name': 'Garth Brooks',     'genre': 'country'},
    {'name': 'Duke Ellington',   'genre': 'jazz'},
    {'name': 'William Shatner',  'genre': 'spoken word'},
    {'name': 'Madonna',          'genre': 'pop'},
]

for a in music:
    print a['name'], ":", a['genre']

print '#--------------------------------------'
print '# yield'
print '#--------------------------------------'
def countdown(n):
    print "counting down:",
    while n>0:
        yield n
        n -= 1

for i in countdown(5):
    print i,
print ""

print '#--------------------------------------'
print '# exception'
print '#--------------------------------------'
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"

divide(4,2)
divide(2,0)


print '#--------------------------------------'
print '# math'
print '#--------------------------------------'

import math

def primes(n):
    nums = range(1,n+1)
    for i in range(2,int(math.sqrt(n))):
        nums = filter(lambda x: x == i or (x%i)!=0, nums)
    return nums    

print primes(20)