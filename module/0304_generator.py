from collections import Iterable
from collections import Iterator
from itertools import islice

'''
python中的生成器（generator）总结
'''

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b


def my_gen(lgth):
    for i in lgth:
        yield i

'''

aa=[1,2,'a',33,'zz']
print(type(aa))
gen=my_gen(aa)
print(type(gen))
print(type(aa))
#print(gen.__next__())
#print(gen.__next__())

list=range(10)
g1=(i for i in list)
print(type(g1))

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance('spring',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(168,Iterable))

print('[] is a Iterator: ?',isinstance([],Iterator))
print('iter([]) is a Iterator: ?',isinstance(iter([]),Iterator))

print('"abc" is a Iterator: ?',isinstance('abc',Iterator))
print('iter("abc") is a Iterator: ?',isinstance(iter('abc'),Iterator))
'''

f=fib()
print(list(islice(f,10)))
