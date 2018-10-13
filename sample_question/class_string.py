"""define class and getstring,printstring to console input print.The input can be uppercase"""

#define class method

class IOString():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):


#print str1 uppercase

        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()


