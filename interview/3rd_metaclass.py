'''
def monkey_patch(name,bases,dct):
    assert(len(bases)==1)
    base=bases[0]
    for name,value in dct.items():
        if name not in ('__module__','__metaclass__'):
            setattr(base,name,value)
    return base


class A(object):
    def a(self):
        print('i am A object')


class PatchA(A,metaclass=monkey_patch('class',object,None)):
    def patcha_method(self):
        print('This is a method patched for class A')


def main():
    pa=PatchA()
    pa.patcha_method()
    pa.a()
    print('dir(pa)=',dir(pa))
    print('dir(PatchA)=',dir(PatchA))


if __name__ == '__main__':
#    main()

'''

class Borg(object):
    _state={}
    def __new__(cls, *args, **kwargs):
        ob=super(Borg,cls).__new__(cls, *args, **kwargs)
        ob.__dict__=cls._state
        return  ob

class MyClass2(Borg):
    a=1