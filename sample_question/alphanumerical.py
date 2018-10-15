"""Find the words as input and print the words after removing all duplicate words and sort   them alphanumerical"""

#assign input
s = input()
words = [word for word in s.split(" ")]

#print the sorted words
print(','.join(sorted(list(set(words)))))
