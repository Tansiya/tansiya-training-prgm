"""assign a class"""
class adm():
	
	""" Create function for adding two number"""
	def addition(a,b):
		c = a+b
		return c

	""" Create function for adding two number"""
	def subtraction(a,b):
		c = a-b
		return c

	""" Create function for adding two number"""
	def multiply(a,b):
		c = a*b
		return c



"""assign variable values"""
a = int(input())
b = int(input())
c = int(input())

"""calling functions"""

result={}
result["addition"] = adm.addition(a,b)
result["subtraction"] = adm.subtraction(a,b)
result["mutiply"] = adm.multiply(a,b)
print("Result is:",result)










	
