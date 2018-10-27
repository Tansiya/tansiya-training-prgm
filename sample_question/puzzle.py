"""Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?"""

#create a function

def solve(numheads,numlegs):
    ns='No solutions!'

#access the for loop

    for i in range(numheads+1):
        j=numheads-i

#using if condition

        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

#assigned the num of heads and legs

numheads=35
numlegs=94

solutions=solve(numheads,numlegs)

print (solutions)

