class testPrivate:
    'how to debug private member and function'
    def __init__(self):
        self.__data=[]

    def add(self,item):
        self.__data.append(item)

    def printData(self):
        print(self.__data)

class Word(str):
    def __eq__(self, other):
        return len(self) == len(other)






'''
w1=Word('asd')
w2=Word('aaa')


print('{}=={}?{}'.format(w1,w2,w1==w2))
print('asd==168?{}'.format('asd'=='168'))


sub1="python string"
sub2="an arg"

a="I am a %s" %sub1
b="I am a {}".format(sub2)

c="with %(kwarg)s!" %{'kwarg':sub2}
d="with {kwarg}!".format(kwarg=sub2)

name=(1,2,3)
print("hi there {}".format(name))
print(a)
print(b)
print(c)
print(d)
print(str(1234))
print(repr(1234))

#如何输出时制定不换行，默认时要换行的
for x in range(0,10):
    print(x,end='')
'''



'''
print('1:\t{0:^10}====='.format('luojian'))
print('1:\t{0:^10}====='.format('zhan'))


'''


"""
   
t=testPrivate()
t.add('dacinggrain')
t.add('Spring')
t.printData()
print(t._testPrivate__data)

"""