"""define a function that can accept an integer number as input print the number is even,otherwise print it is an odd number"""

#create function and check value
def checkValue(n):
#use % operator to check if a number is even or odd 
	if n%2 == 0:
		print ("It is an even number")
	else:
		print ("It is an odd number")
		

checkValue(9)
