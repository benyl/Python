#! /usr/bin/env python

# a simple example in python

principal = 1000
rate = 0.05
numyears = 10

for year in range(1, numyears):
    principal = principal * (1 + rate)
    print "%3d %0.2f" % (year, principal)
