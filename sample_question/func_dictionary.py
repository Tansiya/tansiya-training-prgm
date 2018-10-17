"""function using dictionary key numbers are between 1 and 3 and another key number range between(1,21) the values are square of keys"""

#create fuunction using dictionarySolution
def printDict():
	d=dict()
	for i in range(1,21):
#use the ** operator to get power of number
		d[i]=i**2
#range of for loop
	for (k,v) in d.items():
#to get key/value pairs	
		print (v)
		

printDict()


def printDict():
	d=dict()
#range of for loop
	for i in range(1,21):
#use the ** operator to get power of number
		d[i]=i**2
	for k in d.keys():
#to get key/values pairs	
		print (k)
		

printDict()



def printDict():
	d=dict()
#use ** operator get power of number
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print(d)

#print dictionary key number square value
printDict()



def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print (d)
			
#print dictionary key number square value
printDict()

