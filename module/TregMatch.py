import re

#matchObj=re.match('www','www.baidu.com')
#print(re.match('www','www.baidu.com').span())
#print(re.match('com','www.baidu.com'))

mo=re.match('a.*b','accbammb')
print(mo.group(0))

mo=re.match('a.*?b','accbammb')
print(mo.group(0))

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))