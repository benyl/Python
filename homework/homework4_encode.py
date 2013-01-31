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

# module encode
import sys, pickle
from homework4_gen_key import Key

class EncodeException(Exception):
    "Encode Exception"

def encode(plaintext, key):
    try:
        return [[1] * key[c] for c in plaintext]
    except KeyError:
        raise EncodeException(\
            "encode plain text \"%s\" error" % plaintext)
    

def main():
    
    if len(sys.argv) != 3:
        keyfile = 'pickled_Key.pickle' # default keyfile
        encodefile = 'pickled_encode.pickle' # default keyfile
        print "no path provided, key file: %s, cipher file: %s" %\
              (keyfile, encodefile)
    else:
        keyfile = sys.argv[1] # default keyfile
        encodefile = sys.argv[2] # default keyfile
        print "pickle to file:", keyfile
        
    # load key from pickle file
    with open(keyfile,'r') as f_key, open(encodefile,'w') as f_enc:
        k = pickle.load(f_key)

        # encode the plain text
        cipherlist = []
        while not cipherlist:
            plaintext = raw_input('input plaintext: ').upper()
            
            try:
                cipherlist = encode(plaintext, k)
            except EncodeException as e:
                print "%s\nplease input again\n" % e

        # invoke some error for testing
        mid = int(len(cipherlist)/2)
        cipherlist = [100] + cipherlist[:mid+1] + [[1]*50] + cipherlist[mid+1:]

        print "plain text is:", plaintext
        print "cipher text is:", cipherlist
        
        # pickle the cipher list to file
        pickle.dump(cipherlist, f_enc)
        print 'encode plaintext successed.'

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 2 - Object Serialization and Command Line Arguments'
    print '#--------------------------------------'
    
    print '\n# encode : \n'
    main()

