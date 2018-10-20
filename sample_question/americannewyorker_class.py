"""Define a class named american and subclass newyorker which has a static method call print nationality""" 

#Define class static method
class American(object):
    @staticmethod
#use the function
    def printNationality():
#print the static
        print ("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

#Define a subclass
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
anNewYorker = NewYorker()
print (anAmerican)
print (anNewYorker)



