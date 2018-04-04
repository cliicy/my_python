def foo(x):
    print('executing foo(%s)'%x)


class A(object):
    def foo(self,x):
        print("executing A's foo(%s,%s)" %(self,x))

    @classmethod
    def class_foo(cls,x):
         print('executing class_foo(%s,%s)' %(cls,x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' %x)

'''

#foo('hello')
#foo(128)
a=A()
a.foo('Morning')
a.class_foo('haha')
a.static_foo('Hungry')
'''


class Person:
    name = []

'''

p1 = Person()
p2 = Person()
p1.name.append(1)
print(p1.name)
print(p2.name)
print(Person.name)
'''

aa={'a':'Japan','b':'USA','c':'Canada','d':'China','e':'srilanka','f':'Singapore'}
#for key,value in aa:
'''

for key,value in aa.items():
    print(key,value)
'''

'''

d = {key: value for (key, value) in aa.items()}
print(d)
'''

'''

name=[1,2,3]
print('hi, there is %s' %(name,))

bb='Hi,there is {}'.format(name)
print(bb)
'''

sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0} {1}".format(sub2,sub1)
print(b)

'''


c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a    # "i am a python string!"
print b    # "i am a python string!"
print c    # "with an arg!"
print d    # "with an arg!"

'''