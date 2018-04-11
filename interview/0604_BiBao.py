'''
闭包就是一个定义在函数内部的函数，闭包使得变量即使脱离了
该函数的作用域范围也依然能被访问到。
Lambda表达式就是：能嵌入到其他表达式当中的匿名函数（闭包）。
'''

def my_add(n):
    return lambda x:x+n

add_3=my_add(3)
print(add_3(7))