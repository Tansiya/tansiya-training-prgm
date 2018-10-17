"""define function which can generate  print a tuple where the value are square of numbers between 1 and 20(both included) and print the first half values one line and the last half values in one line, and print the even values"""

#create function using tuple
def printTuple():
	li=list()
#use range of for loop
	for i in range(1,21):
#use list.append and ** operator to get power of value
		li.append(i**2)
#use tuple to get a tuple from list
	print (tuple(li))
		
printTuple()


#tuple values are assiend
tp=(1,2,3,4,5,6,7,8,9,10)
#use [n1+n2] to get a slice from a tuple
tp1=tp[:5]
tp2=tp[5:]
print (tp1)
print (tp2)


tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
#use range of for loop
for i in tp:
	if i%2==0:
#use tuple to generate a tuple from a list
		li.append([i])

tp2=tuple(li)
print (tp2)



