
def xfab(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1


def yfab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1


#fab(5)
'''

for n in yfab(5):
    print(n)
'''

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


f1=Fab(5)
print(type(f1))
print('f1:',f1.next())

print(Fab(5).next())


'''

print(type(range(5)))

print(range(1,5))

for i in range(1000):
    print(type(i))
    pass
'''