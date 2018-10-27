"""Genrate a float random where the values between (10-100),(0-95)and even number between (0-10) then randomly genrate a list 5 even numbers between(100-200).Then therandomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive and  randomly print a integer number between 7 and 15 inclusive. using python math module"""

#Use import for all math function

import random

#Use random.random() to generate a random float in [0,1].

print (random.random()*100-5)

import random

#Use random.random() to generate a random float in [0,1].

print(random.random()*100)

import random

#Use random.choice() to a random element from a list.

print (random.choice([i for i in range(11) if i%2==0]))

import random

#Use random.choice() to a random element from a list.

print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))

import random

#Use random.randrange() to a random integer in a given range.

print (random.randrange(7,15))

