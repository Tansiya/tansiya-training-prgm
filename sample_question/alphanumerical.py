"""Find the words as input and print the words after removing all duplicate words and sorting them alphanumerically"""

#assign a input
n = input()
words = [word for word in s.split(',')]

	#print the words
print(''.join(sorted(list(set(words)))) 
