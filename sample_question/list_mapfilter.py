"""The program which can map() and filter() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]"""

#use map to generate a list

li = [1,2,3,4,5,6,7,8,9,10]
#use lambda to define anonymous function

squaredNumbers = map(lambda x: x**2, li)

print (squaredNumbers)


li = [1,2,3,4,5,6,7,8,9,10]

#use filter to filter elements of a list

evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))

print (evenNumbers)

