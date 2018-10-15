"""calculate the number of letters and  digits"""

#assign a values
s = input()
#using dictionary
d={"DIGITS":0, "LETTERS":0}
#access for the values
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
#print number of letters and digits
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])
