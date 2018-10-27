""" write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"""

#import for use all math operation

import zlib

#assiend the string

s = 'hello world!hello world!hello world!hello world!'

t = zlib.compress(s)

#print compress

print (t)

#print decompress

print (zlib.decompress(t))
