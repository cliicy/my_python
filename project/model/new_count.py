from count import A


class Test(object):
    def __init__(self,world):
        self.world=world

    def __str__(self):
        return 'world is %s str' %self.world

    def __repr__(self):
        return 'world is %s repr' %self.world

    def __example(self):
        self.__data='hello'
        print(self.__data)


class B(A):
    def sub(self,a,b):
        return a-b





"""
t=Test('world_big')
print(str(t))
print(repr(t))

result = B().add(2,5)
print(result)
"""