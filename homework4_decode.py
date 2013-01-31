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


# module decode
import sys, pickle
from homework4_gen_key import Key

class DecodeException(Exception):
    "Decode Exception"

def decode(cipherlist, key):

    # reverse the key and value
    rev_key = {v:k for k,v in key.items()}

    # return ''.join([rev_key[len(l)] for l in cipherlist])
        
    try:
        plainlist = []
        for l in cipherlist:
            try:
                plainlist.append(rev_key[len(l)])
            except (KeyError,TypeError) as e:
                etype = "KeyError" if isinstance(e, KeyError) else "TypeError"
                print "decode error: %s - %s" % (etype, e)
                continue
        return "".join(plainlist)
    except TypeError:
        raise DecodeException("decode error: cipher text is not a list")
    

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
        
    # load key from pickle file & decode the cipher text
    with open(keyfile,'r') as f_key, open(encodefile,'r') as f_enc:
        
        k = pickle.load(f_key)
        cipherlist = pickle.load(f_enc)
        
        try:
            print "cipher text is:", cipherlist
            
            plaintext = decode(cipherlist, k)
            
            print "plain text is:", plaintext
        except DecodeException as e:
            print e
            

if __name__ == "__main__": # Default "main method" idiom.
    print '#--------------------------------------'
    print '# Part 2 - Object Serialization and Command Line Arguments'
    print '#--------------------------------------'
    
    print '\n# decode : \n'
    main()

