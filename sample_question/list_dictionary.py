"""Define a function and print a list where the values are square of numbers between 1 and 20(both included).the function needs first 5 elementsin list and last 5 elements in the list otherwise prints all vales except first 5 elements in the list"""

#create function to use list
def printList():
	li=list()
#use range of for loop
	for i in range(1,21):
#use list.append and add values into a list 
		li.append(i**2)
	print (li)
		

printList()


def printList():
	li=list()
#use range of for loop
	for i in range(1,21):
#use list.append and ** to get power of number
		li.append(i**2)
#use[n1:n2] to slice a list
	print (li[:5])
		

printList()


def printList():
	li=list()
#use range of for loop
	for i in range(1,21):
#use list.append and ** operator to get power of number
		li.append(i**2)
#use[n1+n2] to slice a list
	print (li[5:])
		

printList()


def printList():
	li=list()
#range of for loop
	for i in range(1,21):
#use list.append and ** to get power of number
		li.append(i**2)
#use[n1:n2] to slice a list
	print (li[-5:])
		

printList()

