from T1703 import A


class B(A):
    def sub(self,a,b):
        return a-b


result = B().add(2,5)
print(result)