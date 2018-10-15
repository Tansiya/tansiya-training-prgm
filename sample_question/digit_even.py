"""Find all numbers between 1000 and 3000 (both included) such that each of the number is even number"""

#assign values

values = []

#access for the range

for i in range(1000, 3001):
    s = str(i)

    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):

#append s

        values.append(s)
print (",".join(values))
