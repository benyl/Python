###############################################
# COMS3101.003 - Python - Homework 4
#

################################################
# Part 2 - Object Serialization and Command Line Arguments
#
# (a) Write a module 'gen_key', that contains a class Key with base
#     class dict. When Key instances are initialized they should
#     randomly map each of the 26 English letters [A-Z] and whitespace
#     to a unique ciphertext number between 0 and 26.
# (b) Write a module 'encode', that contains a function encode, which 
# 	  takes as parameters a plaintext message and a key instance and 
#     encodes the message in the following simple unary representation.
#     The message is represented as a list and each element of the list
#     represents a letter. 
# (c) Write a module 'decode', that contains a function decode, which 
#     takes as parameters an encoded message object, of the type described
#     above, and a Key object, and returns a plaintext string.
#     Write a main function that unplickes a message object and a Key 
#     object from a file, uses decode to decode the message and prints
#     the plaintext. 

################################################
# Part 3 - Exceptions
#
# (a) When encoding a message, the plaintext may contain symbols other 
#     than 26 letters or space. In the 'encode' module, create an 
#     exception class EncodingException and raise an exception on this
#     type in the encode function when an input symbol cannot be encoded.
#     Modify the main method to handle this exception.
# (b) The object to be decoded is not a valid encrypted message.
#     This can be case for a number of reasons.
#     1. The message object is not a list at all. 
#     2. The outer list contains a non-list element.
#     3. There are too many elements in one of the inner lists.
#     Implement this behavior and provide examples for objects causing 
#     each type of exception.

# module gen_key
import sys, random, pickle

class Key(dict):
    
    def __init__(self):
        
        words = [' '] + [chr(i) for i in range(ord('A'),ord('Z')+1)]

        for i in range(27):
            w = random.choice(words)
            self[w] = i
            words.remove(w)


def main():
    
    if len(sys.argv) != 2:
        filename = 'pickled_Key.pickle' # default filename
        print "no path provided, pickle to file:", filename
    else:
        filename = sys.argv[1]
        print "pickle to file:", filename
        
    # generate key and pickle to file
    k = Key()
    with open(filename,'w') as f:
        pickle.dump(k, f)
        
    print k

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 2 - Object Serialization and Command Line Arguments'
    print '#--------------------------------------'
    
    print '\n# gen_key : \n'
    main()

