""" Usage: Find and calculate the square root value.print the input single or list variable"'""

"""assign a import for all maths function"""

import math

"""assign a fixed values of C and H"""

c = 50
h = 30

value = []
items = [x for x in input().split(',')]

"""creating for loop function"""

for d in items:

"""calculate the square root formula"""

	value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

"""print the input list or single variable"""

print(','.join(value))
