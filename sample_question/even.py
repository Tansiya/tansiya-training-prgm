"""we can write a program even numbers and divisible by 5,7 and 0 between 0 and n.Print the even values and divisible values""" 

#create function using evengenerator

def EvenGenerator(n):
    i=0
#use the while condition

    while i<=n:

#using if loop

        if i%2==0:

#use yield to produce nextvalue generate

           yield i

        i+=1

#assign the input

n=int(input())

values = []

#access for values

for i in EvenGenerator(n):

    values.append(str(i))

#print evennumbers only

print (",".join(values))





