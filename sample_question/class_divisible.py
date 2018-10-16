"""define a class generate which can iterate the number,which divisible by 7,range between 0 and n"""
#assign a function
def putNumbers(n):
    i = 0
#using while loop
    while i<n:
        j=i
        i=i+1
#using if loop
        if j%7==0:
            yield j
#access for reverse
reverse = int()
for i in reverse(100):
#print i
    print (i)
