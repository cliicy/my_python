#import sys
#sys.path.append("./model")
from model import new_count
from model import count

"""
'cannot invoke the private function in a class'
t=new_count.Test("Luo")
t.__example()
"""

'''
print(dir(new_count))
print("__doc__=",new_count.__doc__)
print("result=",new_count.result)
print("__file__=",new_count.__file__)
print("__builtins__=",new_count.__builtins__)
print("__name__=",new_count.__name__)
print("__package__=",new_count.__package__)
print("__spec__=",new_count.__spec__)
print("__cached__=",new_count.__cached__)
#new_count(__doc__)


tt=new_count.B()
tt.add(2,5)
print(tt.add.__doc__)

MyName={}
myC = count.A()
myC.init(MyName)
myC.store(MyName,'Jianjun Luo Sun','Xiaohong Luo Tiger')
print(myC.lookup(MyName,'middle','Luo'))
'''

