import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
print(b is a )
c = copy.copy(a)  # 对象拷贝，浅拷贝
print(c is a )
d = copy.deepcopy(a)  # 对象拷贝，深拷贝
print(d is a )

a.append(5)  # 修改对象a
print(b is a )
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)


names = ["小明", "小红", "小黑", "小黄", "小白"]
# 把 names 复制，赋值给 names 变量
names2 = names.copy()
# 修改 names 列表中的 小黄
names[3] = "Yellow"
# 分别输出 names names2
print(names)
print(names2)

names = ["小明", "小红", ["张三", "李四", "王五"], "小黑", "小黄", "小白"]
# 复制一份列表
names2 = names.copy()
# 把李四 改成英文
names[2][1] = "Lisi"
print(names)
print(names2)