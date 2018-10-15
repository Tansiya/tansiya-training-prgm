"""Find the net amount of a bank account transaction log from console input print.The transaction log amount(d=100, 200)"""

#assign a net amount
net = 0

while True:
	line = input("> ").split()
	if not line:
		break;
		
	amt = int(line[1])
	if line[0] == 'D':
		net += amt
	elif line[0] == 'W':
		net -= amt
#Priint the net amount
print (net)

