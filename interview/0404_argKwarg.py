'''

def test_fun(*args):
    nl=len(args)
    print(nl)
    print(args)


test_fun('spring','summer','autumn','winter')


def test2_fun(**kwargs):
    for value, item in kwargs.items():
        print(value,item)


test2_fun(spring='1-3',summer='4-6',autumn='7-9',winter='10-12')
'''

'''

def foo(*args,**kwargs):
    print('args=',args)
    print('kwargs=',kwargs)
    print('---------------')


foo(1,2,3,4)
foo(a=1,b=2,c=3)
foo(1,2,3,4,a=1,b=2,c=3)
foo('a',1,None,a=1,b='2',c=3)


def kw_dict(**kwargs):
    return kwargs


print(kw_dict(a=1, b=2, c=3) == {'a': 1, 'b': 2, 'c': 3})
'''