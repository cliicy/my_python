import shelve

s=shelve.open('myshelve.dat')
s['x']=['a','b','c']
s['x'].append('d')
print(s['x'])


tmp=s['x']
tmp.append('d')
s['x']=tmp
print(s['x'])