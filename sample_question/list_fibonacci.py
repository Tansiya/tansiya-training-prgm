"""We can write the recursive function using program and use the listcomprehensive.use string.join print the join to a list of strings"""

#create recursive function in python
def f(n):
#use the if loop
    if n == 0: return 0
#use eflif loop
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())

#use list comprehensive to generate a list from an existing list

values = [str(f(x)) for x in range(0, n+1)]

#use string.join() to join a list of strings

print (",".join(values))



