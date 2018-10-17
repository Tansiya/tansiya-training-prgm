"""using function that can accept two strings as input and print the maximum length.two strings the same length then print the function line by line"""

#create function to get the length of a string
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
#using if loop condition
	if len1>len2:
		print (s1)
	elif len2>len1:
		print (s2)
	else:
		print (s1)
		print (s2)
		
#print the function 
printValue("seven","seven")
