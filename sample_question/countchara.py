"""Write a program to count and print the numbers of each character in a string input by console"""

#Create dictionary to store key value pair

dic = {}
s=input()

#access values for loop
for s in s:
    dic[s] = dic.get(s,0)+1

#print the number characters

print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

