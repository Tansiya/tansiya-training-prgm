"""The program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]"""

#use map to generate a list
li = [1,2,3,4,5,6,7,8,9,10]
#use lambda to define anonymous function
squaredNumbers = map(lambda x: x**2, li)

print (squaredNumbers)
