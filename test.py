1.linux is a opensource operating system...which is modelled by unix.
	commands:
	ls-list
	pwd-print working directory
	touch-file creating
	nano-file editor
	if confg-check system IP address

2.linux kernal:
	kernal is the core of the linux terminal.which is sceduled process and interface directly with the hardware.then manage the system and user i/o.

3.diff b/w 32bit&64bit:
	the terms of "32-bit" and "64-bit" are commonly seen in system requirements.
	the 64-bit version of windows handles large amount of data compared to 32-bit processor
	the 32-bit processor can process 32 digits at a time whereas 64-bit handle 64digit
	we have maximum memory space access 64bit
4.git:

    git is a file transfer.
	git configure,
	git clone
	,git push
	git pull	

version:
    2.17.0

6.low level &high level language:
LOW LEVEL LANGUAGE:
	low level languages are machine dependent programming languages such as binary and assembly language.
	since computer only understand binary language that vmachines instructions in the form of 0's and 1's.
Eg:
	c,c++
HIGH LEVEL:
	a high level languages is an advanced computer programming that abstracts details of the undelying hardware.the machine independent programming languages vwhich  are  easy to write,read,edit and understand
eg:
  java,.net,pascal,cobol,
	

7.object:
python is a great programming language that supports oop.you will use it to define a class with attributes and methods.python offers a number of benefits compared to other programming language.
object oriented programming is based on the imperative programming paradigm.
Eg:
	class employee
	private string name;
	public string get name()
	return name;
	
8.Linux distribution name:
	* Fedora release 28 (Twenty Eight)
kernal version:
	Linux 4.16.3-30-amdX86_64
	cat /etc/os-releaseimport platform
import sys

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))
output:
	Python version: ['3.6.5 (default, Mar 29 2018, 18:20:46) ', '[GCC 8.0.1 20180317 (Red Hat 8.0.1-0.19)]']
dist: ('fedora', '28', 'Twenty Eight')
linux_distribution: ('Fedora', '28', 'Twenty Eight')
system: Linux
machine: x86_64
platform: Linux-4.16.3-301.fc28.x86_64-x86_64-with-fedora-28-Twenty_Eight
uname: uname_result(system='Linux', node='localhost.localdomain', release='4.16.3-301.fc28.x86_64', version='#1 SMP Mon Apr 23 21:59:58 UTC 2018', machine='x86_64', processor='x86_64')
version: #1 SMP Mon Apr 23 21:59:58 UTC 2018
mac_ver: ('', ('', '', ''), '')



9."""assign a class"""
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

10.def frog(): 
	divi =['jasmine', 'lotus', 'tulip']
	for c, value in enumerate(divi, 1):
		print(c, value)

frog()
output:
1 jasmine
2 lotus
3 tulip

5.Gitub accout and make a repository:
	github account name:Tansiya-training-prgm
	user name:Tansiya	  	
