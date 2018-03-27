import re
import pprint

st=re.search('(python\.org)','http_python.org')
print(st.groups(0))

st=re.search('(.*?org.*)','http_python.org')
print(st.groups(0))

st=re.search('[pj]ython','http_python.orgjython')
print(st)

st=re.findall('[pj]ython','http_python.orgjython')
print(st)

st=re.search('p(ython|erl)','perlpython')
print('aa',st.groups())

ss='http://www.python.org'
ss1='http://python.org'
ss2='www.python.org'
ss3='python.org'
sp=r'((http)?(www\.)?python\.org)'
r1=re.search(sp,ss)
print('r1',r1.groups())

print('r2',re.search(sp,ss1))
#print('r2',r2.groups())

some_text='alpha, beta,,,,gama delta'
print(re.split('[, ]+',some_text))

print(re.split('o(o)','foobar'))#如果模式包含小括号，那么括起来的字符组合会散布在分割后的子字符之间

print(re.split('o','foobar'))

print(re.split('[. ]+',some_text,maxsplit=2))
print(re.split('[. ]+',some_text,maxsplit=1))

text='"Hm...Err -- are you sure?" he said,sounding insecure'
pat=r'[.?\-".]+'
print(re.findall(pat,text))

pat='{name}'
text='dear {name}...'
print(re.sub(pat,'Mr. Gumby',text))

print(re.escape('www.python.org'))
print(re.escape('But where is the ambiguity?'))

m=re.match(r'www\.(.*)\..{3}','www.python.org')
print(m.group(1))
print(m.start(1))
print(m.end(1))
print(m.span(1))


emphasis_pattern=r'\*([^\*]+)\*'
print(re.sub(emphasis_pattern,r'<em>\1</em>','Hello,*world*!'))