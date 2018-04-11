from warnings import warn
from types import FunctionType


def login_required(func):
    print('login check logic here')
    return func


class LoginDecorator(type):
    def __new__(cls, name,bases,dct):
        for name,value in dct.items():
            if name not in ('__metaclass__','__init__','__module__') and type(value) == FunctionType:
                value=login_required(value)
            dct[name]=value
        return type.__new__(cls,name,bases,dct)

class Operation(object,metaclass=LoginDecorator):
    def delete(self,x):
        print('deleted %s' %str(x))


def main():
    op=Operation()
    op.delete('test')


if __name__ == '__main__':
    main()


'''

def ma(cls):
    print('method a')


def mb(cls):
    print('method b')


method_dict = {
    'ma': ma,
    'mb': mb,
}

class myDynamicMethord(type):
    def __new__(cls, name, bases,dct):
        if name[:3]=='Abc':
            dct.update(method_dict)
        return type.__new__(cls,name,bases,dct)

    def __init__(cls,name,bases,dct):
        super(myDynamicMethord,cls).__init__(name,bases,dct)

class AbcTest(object,metaclass=myDynamicMethord):
    def mc(self,x):
        print(x*3)


class NotAbc(object,metaclass=myDynamicMethord):
    def md(self,x):
        print(x*3)


def main():
    a=AbcTest()
    a.mc(3)
    a.ma()
    print('dir(a)=',dir(a))

    b=NotAbc()
    print('dir(b)=',dir(b))

class ReqStrSugRepr(type):
    def __init__(cls,name,bases,attrd):
        super(ReqStrSugRepr.cls).__init__(name,bases,attrd)
        if '__str__' not in attrd:
            raise TypeError('Class requires overridig of __str__()')

        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n',stacklevel=3)

class Foo(object,metaclass=ReqStrSugRepr):
    def foo(self):
        pass

fo=Foo()
fo.foo()

X=type('X',(object,),dict(a=1))
print(X)

def say(self):
    print('hello')

S=type('S',(object,),dict(say=say))
s=S()
s.say()
'''

'''

class PrivateMetaclass(type):
    def __new__(cls, name, parents, attrs):
        attrs = dict(('__%s' % k, v) for k, v in attrs.itmes())
        return super(PrivateMetaclass, cls).__new__(cls, name, parents, attrs)


class A(object,metaclass=PrivateMetaclass):
    a = 1
    b = 2


a = A()
print(a.a,a.b)

'''

'''

# metaclass   元类   metaclass允许你创建类或者修改类
class Listmetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)  # 增加了add（）方法
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=Listmetaclass):
    pass


# __new__()方法接收到的参数依次是：

# 1、当前准备创建的类的对象；
# 2、类的名字；
# 3、类继承的父类集合；
# 4、类的方法集合。


# 元类一般情况不常用，但总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，
# 也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

L = MyList()
L.add(2)  #增加了add（）方法
L.add(3)
print(L)

'''

'''
if __name__ == '__main__':
    main()



def metaclass_new(name,bases,attrs):
    print(name,bases,attrs)


class test_fromMetaFun(metaclass=metaclass_new):
    print("test_fromMetaFun")


class test_fromMetaClass(object,metaclass=myDynamicMethord):
    print("test_fromMetaClass")

'''
