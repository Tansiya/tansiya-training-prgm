"""write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]"""

#assigned the subject

subjects=["I", "You"]

verbs=["Play", "Love"]

objects=["Hockey","Football"]

#acces the values for loop i,j,k

for i in range(len(subjects)):

    for j in range(len(verbs)):

        for k in range(len(objects)):

            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])

#print sentence
            print (sentence)
