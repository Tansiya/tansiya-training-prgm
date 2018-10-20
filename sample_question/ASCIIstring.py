"""Program to read an ASCII string and convert it to aunicode string encoded by utfp-8"""


#Define input s

s=input()

#Use unicode function to convert

U = Unicode( s ,"utf-8")

#print the unicodestring encoded

print (U)

