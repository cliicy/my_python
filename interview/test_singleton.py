from mysingleton import my_singleton
from mysingleton import MyClass

print(type(my_singleton))
my_singleton.foo()
'''

one = MyClass()
two=MyClass()
print(one==two)

print(one is two)

print(id(one))
print(id(two))
'''