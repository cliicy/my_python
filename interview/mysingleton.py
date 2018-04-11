from functools import wraps


#'''
def singleton(cls):
    isinstance={}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        if cls not in isinstance:
            isinstance[cls]=cls(*args,**kwargs)
        return  isinstance[cls]
    return  getinstance

@singleton
class MyClass(object):
    a=1


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass
#'''


'''
原始的方法创建一个singleton对象
'''
#'''

class My_singleton(object):
    def foo(self):
        pass

my_singleton=My_singleton()
#'''


'''
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1

'''