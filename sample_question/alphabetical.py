
"""find the input and print.The words in sorting them alphabetically"""

#creat items

items = [x for x in input().split(',')]

#the words are sorting

items.sort()

#print the items

print(','.join(items))
