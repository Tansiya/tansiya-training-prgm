"""we can write the program to find fibonacci series by given input"""

#create the function

def f(n):

#use the if loop

    if n == 0:
 
return 0

#use elif loop

    elif n == 1:
 
return 1

    else:

 return f(n-1)+f(n-2)

#define the input

n=int(input())

print(f(n))
