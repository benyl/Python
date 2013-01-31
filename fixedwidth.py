#! /usr/bin/env python

# a function like str_pad in PHP
def fixedwidth(value, arg):
    """
    Truncates or pads a string to be a certain length
    
    Argument: Desired length of string
    """

    try:
        length = int(arg)
    except ValueError: # invalid literal for int()
        return value # Fail silently
    if not isinstance(value, basestring):
        value = str(value)

    if len(value) > (length):
        value = value[:length - 3]
        value += '...'
    elif len(value) < length:
        for _ in range((length - len(value))/2):
            value = " " + value
            value = value + " "
        if ((length - len(value))%2):
            value = value + " "
    
    return value.replace(" ", "&nbsp;") # replace with &nbsp for html

str = "at&t and btet"
print str.split()
print len(str)

str = fixedwidth(str, 20)
print str
