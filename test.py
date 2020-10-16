import re

obj = re.search('he','hello!')

print(obj.group())
print(obj.start())
print(obj.end())
print(obj.span())