"""The program which can filter even numbers in a list by using filter function.the list is:[1,2,3,4,5,6,7,8,9,10]"""

#use function to filter some elements in a list

li = [1,2,3,4,5,6,7,8,9,10]

#use lambda to define anonymous function

evenNumbers = filter(lambda x: x%2==0, li)

#print the evennumbers

print (evenNumbers)

 
