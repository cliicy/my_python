def print_pars(*params):
    print(params)


def print_pars2(title,*params):
    print(title)
    print(params)


def print_pars3(**params):
    print(params)


def print_pars4(x,y,z=3, *pospar, **keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)


def interval(start,stop=None,step=1):
    'Imitates range() for step>0'
    if stop is None:
        start,stop=0,start
    result=[]
    i = start
    while i<stop :
        result.append(i)
        i+=step
    return result


def power(x,y,*others):
    if others:
        print('Receive redundant parameters:', others)
    return pow(x,y)


def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor


def factorial(n):
    result=n
    for i in range(1,n):
        result *=1
    return result

def charnum(x):
    return x.isalnum()

seq=['foo','x41','?!','***']
tt=[x for x in seq if x.isalnum()]
#print(tt)
res= filter(charnum,seq)
for n in res:
    print(n)

t2=filter(lambda  x:x.isalnum,seq)
for n2 in t2:
    print(n2)


def find_str(str):
    index=0
    for string in str:
        if 'abc' in string:
            str[index]='[censored]'
        index+=1
    print(str)

find_str(['lalalaaxxabchaha','abcc','cdd'])

s1=str(1)
s2=str(2)




"""
factorial(3)
double = multiplier(2)
print(double(5))

triple=multiplier(3)
print(triple(3))

t1=multiplier(5)(4)
print(t1)
tt=(5,)*2
print(tt)

interval(10)
interval(1,5)
interval(3,12,4)
power(*interval(3,7))



print_pars('testing')
print_pars(1,2,3)

print_pars2('Params2:', 1, 2, 3)
print_pars2('Nothing')

print_pars3(x=1,y=2,z=3)

print_pars4(1,2,3,5,6,7,foo=1,bar=2)

"""