import itertools
import sys


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    print(i*2)
    return i * 2


# 使用for循环
for i in yield_test(5):
    pass
    print(i, ",")


'''
def node._get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild

result, candidates = list(), [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result



def g():
    print('1')
    x=yield 'hello'
    print('2','x=',x)
    y=5+(yield x)
    print('3','y=',y)


f=g()
#f.next()


mylist = [x*x for x in range(3)]
for i in mylist :
    #print(i)
    pass
'''


mygenerator = (x * x for x in range(3))
for i in mygenerator :
#    print(i)
    pass

'''
def createGenerator():
    mylist=range(3)
    for i in mylist:
        yield i*i
        print('a')


mygentor=createGenerator()
print(mygentor)
for i in mygentor:
    print(i)
    
'''
'''
class Bank():
    crisis=False
    def create_atm(self):
        while not self.crisis:
            yield "$100"




hsbc=Bank()
corner_street_atm=hsbc.create_atm()
print(corner_street_atm.__next__())




print(corner_street_atm.__next__())
print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for cash in range(5)])
hsbc.crisis = True
print(corner_street_atm.next())
wall_street_atm = hsbc.create_atm()
print(wall_street_atm.next())
hsbc.crisis = False
print(corner_street_atm.next())
brand_new_atm = hsbc.create_atm()
for cash in brand_new_atm :
    print(cash)

'''

'''
nested=[[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield(element)


for num in flatten(nested):
    print(num)

'''

'''

#排列组合
horses=[1,2,3,4]
races=itertools.permutations(horses)
print(races)
print(list(races))
'''

'''
def h():
    print('to be brave')

    m=yield 5
    print(m)
    d=yield 12
    print('Sleeping')

c=h()
m=c.__next__()
#c.__next__()
d=c.send('FightingAA')
print('we will never forget the date',m,'.',d)
'''


'''

#stdin是一行一行读取的
for line in sys.__stdin__:
    if line.strip():
        print(line,'')
        print('xixi')
        
'''