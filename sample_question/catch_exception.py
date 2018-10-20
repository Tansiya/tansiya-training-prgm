"""Function to compute 5/0 and use try/except to catch the exception"""

#Create function
def throws():
    return 5/0
#Use try/except to catch exceptions
try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except ExceptionError:
    print ("Caught an exception")
finally:
    print ("In finally block for cleanup")


