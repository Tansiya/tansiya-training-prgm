"""Assuming the email addresses in the "username@companyname.com" print the companyname of the given email addresses"""

#Use import for all math operation
import re
#create email addresses
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print (r2.group(2))

