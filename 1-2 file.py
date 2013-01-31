#! /usr/bin/env python

# some example about file read and write

filename = "file.txt"

#-----------------------------
# file write ver.1
#-----------------------------

f = open(filename, "w")

for i in range(1,10):
    f.write("%d\n" % i)

print "file write finfished."
f.close

#-----------------------------
# file read ver.1
#-----------------------------

f = open(filename)
line = f.readline()

while line:
    print line,
    line = f.readline()

print "file read finfished."
f.close


#-----------------------------
# file read ver.2
#-----------------------------

for line in open(filename):
    print line,


#-----------------------------
# file read ver.3
#-----------------------------

fvalues = [int(line) for line in open(filename)]
print fvalues



# another example

filename = "file.txt"

#-----------------------------
# file write with format
#-----------------------------
f = open(filename, "w")
text = """IBM, 100, 16.25
Google, 200, 25.75
Apple, 300, 32.50
HSBC, 150, 13.35
BOA, 250, 20.91"""

f.write(text)
f.seek(0) # jump to head
f.close

#-----------------------------
# file read in format
#-----------------------------
portfolio = []

for line in open(filename):
    fields = line.split(",")
    name   = fields[0]
    shares = int(fields[1])
    price  = float(fields[2])
    stock  = (name, shares, price)
    portfolio.append(stock)

total = 0.0
for name, shares, price in portfolio:
    print name, shares, price
    total += shares * price

print "total = " + str(total)
