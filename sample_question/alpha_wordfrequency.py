"""Find the frquency of the words from the input.output after sorting the key alphanumerically."""

#frequency of words in text
freq = {}  
line = input()
#using for loop
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
print(sorted(set(words)))
words.sort()

for w in words:
#print words in frequency and alphanumerically
    print ("%s:%d" % (w, freq[w]))
