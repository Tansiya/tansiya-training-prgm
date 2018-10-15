"""find and calculate the number of uppercase letters and lowercase letters"""

#assing a input
s = input()
#unsing dictionary
d={"UPPER CASE":0, "LOWER CASE":0}
#access for the values s
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
#print the uppercase and lowercase letters
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])
