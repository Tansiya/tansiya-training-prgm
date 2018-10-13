""" find the factorial number and divide the 7 and but are not a multiple of 5.print the values factorial or list"""

""""assign a factorial and using function"""
def fact(x):
	if (x == 0):
		return 1
	else:
		return x * fact(x - 1)

"""assign a list and using function"""
def maths():
	l= []

"""creating for loop function"""

for i in range(900, 1000):
		if (i%7==0) and (i%5!=0):
			factorial = fact(i)
			l.append(str(factorial))

return l

"""find k value"""
	
k = maths()


"""print the result factorial and list"""

print ("Result is", ','.join(k))
#print ("factorial is", factorial)
	
