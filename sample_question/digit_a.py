"""Find and compute the value of a+aa+aaa+aaaa with given a digit as the value of a"""

#assign a input
a = input()
#find the n1,n2,n3,n4
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
#print the values
print (n1+n2+n3+n4)
