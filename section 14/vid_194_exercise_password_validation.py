# regular expressions

import re

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

string = 'b@b.com'

a = pattern.search(string)
print(a)
print(a)

# PASSWORD CHECKER
#
# pattern that matches a string at least 8 char long
# contain any sort letters, numbers, and symbols $%#@
# has to end with a number

password = 'mysecr444etpass$@3'
pass_pattern = re.compile(r'[a-zA-Z0-9$%#@]{8,}\d')

a = pass_pattern.fullmatch(password)
print(a)
