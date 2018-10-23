"""We can write a program to print divisible numbers between 0 and n with divisible by 5,7 and 0"""

#define the function generate
def NumGenerator(n):
#access for value
    for i in range(n+1):

#use if loop
        if i%5==0 and i%7==0:
#use yield to next value generate

            yield i

#assign the input

n=int(input())

values = []

#access for values

for i in NumGenerator(n):

    values.append(str(i))

print(",".join(values))

