# regular expressions

import re

pattern_0 = re.compile('this')
pattern_1 = re.compile('search inside this')
string = 'search inside this of this text please!'

# returns only one of the matched patterns for 'this'
a = pattern_0.search(string)

print(a.group())

print(a.start())
print(a.end())

# list of matches
b = pattern_0.findall(string)
print(b)

# requires a match of the entire string
c = pattern_0.fullmatch(string)
print(c)

#
d = pattern_1.match(string)
print(d)
