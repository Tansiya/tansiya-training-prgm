"""Write a program which can filter(),map() to make a list elements are evennumbers and squarenumbers between 1 and 20 both included"""

#use filter to filter elements in a list

evenNumbers = filter(lambda x: x%2==0, range(1,21))

#print evenvalues

print (evenNumbers)


#use map to generate a list

squaredNumbers = map(lambda x: x**2, range(1,21))

#print squarevalues

print (squaredNumbers)

