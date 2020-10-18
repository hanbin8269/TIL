import re

p = re.compile('ba?d')

print(p.findall('bd'))
print(p.findall('bad'))
print(p.findall('baaaaaaad'))