import re

p = re.compile('l*')
print(p.findall('loool'))
print(p.findall('l&l'))
print(p.findall('asd'))