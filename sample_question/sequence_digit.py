"""When the program accepts the sequence of words seperated by whitespaceas to print the words composed of digits only"""

#import for using all math operation

import re

s = input()

#print the digits only

print (re.findall("\d+",s))


