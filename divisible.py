def fact(x):
	if (x == 0):
		return 1
	else:
		return x * fact(x - 1)


def maths():
	l= []
	for i in range(900, 1000):
		if (i%7==0) and (i%5!=0):
			factorial = fact(i)
			l.append(str(factorial))

	return l

	
k = maths()

print ("Result is", ','.join(k))
#print ("factorial is", factorial)
	
