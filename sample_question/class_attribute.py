"""Define a custom exception class which takes a string message as attribute"""

#To define a exception
class MyError(Exception):

    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
#create function
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
