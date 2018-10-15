"""Find 4 digit binary numbers as its input and check they are divisible by 5 or not print.the numbers that are divisibleby 5."""

#assign a value
value = []
items=[x for x in input().split(',')]

for p in items:
	print (p)

intp = int(p, 2)
print (intp)

if not intp%5:
        value.append(p)

#print the divisible numbers
print (','.join(value))
