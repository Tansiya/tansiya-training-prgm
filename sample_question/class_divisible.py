"""define a class generate which can iterate the number,which divisible by 7,range between 0 and n"""

#assign a function
class string_handling():
	def putNumbers(n):
		divi = []
		for i in range(1, n+1):
			if i%7==0:
				divi.append(i)
		
		return divi

	def st_rev(n):
		s = str(n)[::-1]
		return s


n = int(input())
b = string_handling.putNumbers(n)
c = string_handling.st_rev(n)
print("Reverse", c)
print("Numbers divisible by 7", b)
