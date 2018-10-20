"""Assuming the email addresses in the "username@companyname.com" format,print the username of a given email address.bothusernames and company names are composed of letters only"""

#import for use all math function

import re

#create email addresses

emailAddress = input()

pat2 = "(\w+)@((\w+\.)+(com))"

r2 = re.match(pat2,emailAddress)

print (r2.group(1))





