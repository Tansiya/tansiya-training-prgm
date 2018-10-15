"""find the squre each odd number in a list.this list is input sequence."""

#assign a input value
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
#print the odd numbers
print (",".join(numbers))
