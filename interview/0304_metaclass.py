'''
class ObjectCreator(object):
    pass


def echo(o):
    print(o)

my_obj=ObjectCreator()
print(my_obj)
print(hasattr(ObjectCreator,'new_attribute'))

ObjectCreator.new_attribute='foo'
print(hasattr(ObjectCreator,'new_attribute'))

print(ObjectCreator.new_attribute)

ObjectCreateMirror=ObjectCreator
print(ObjectCreateMirror())
'''

"""

def choose_class(name):
    if name=='foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


myclass = choose_class('foo')
print(myclass)
print(myclass())

print(type(1))
print(type('1'))

print(type(ObjectCreator))
print(type(ObjectCreator()))

oClass = type('ShinyClass',(),{})
print(oClass)
print(oClass())

#MyClass = MetaClass()
MyClass = type('MyClass', (), {})
MyObject = MyClass()
"""


def ma(cls):
    print('method a')


def mb(cls):
    print('method b')



method_dict = {
    'ma': ma,
    'mb': mb,
}


class DynamicMethod(type):
    def __new__(cls, name, bases, dct):
        if name[:3] == 'Abc':
            dct.update(method_dict)
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(DynamicMethod, cls).__init__(name, bases, dct)


class AbcTest(object,metaclass=DynamicMethod):
    def mc(self, x):
        print( x * 3)


class NotAbc(object,metaclass=DynamicMethod):
    def md(self, x):
        print( x * 3)

def main():
    a = AbcTest()
    a.mc(3)
    a.ma()
    print(dir(a))
    b = NotAbc()
    print( dir(b))



if __name__ == '__main__':
    main()