storage={}
storage['first']={}
storage['middle']={}
storage['last']={}

me='Jianjun Luo Sun'
storage['first']['Jianjun']=[me]
storage['middle']['Luo']=[me]
storage['last']['Sun']=[me]

print(storage)
#print(storage['middle']['Luo'])


my_sister='Anne Luo Sun'
storage['first'].setdefault('Anne',[]).append(my_sister)
storage['middle'].setdefault('Luo',[]).append(my_sister)
storage['last'].setdefault('Sun',[]).append(my_sister)
print(storage['first']['Anne'])
print(storage['middle']['Luo'])

print(storage)