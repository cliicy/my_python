'''


seq=range(5)
enumerate(seq)
print(type(seq))
print(enumerate(seq))

list=['台湾','泰国','日本','菲律宾','马来西亚','斯里兰卡','新加坡','斯里兰卡','加拿大','美国']
for index,item in enumerate(list):
    print(index,item)
print('\n')
for index,item in enumerate(list,1):
    print(index,item)

'''

aa=open('ConfPython.txt','r').readline().strip()
#print(aa)
#count = len(aa)
#print(count)

'''

count=0
for index, line in enumerate(open('ConfPython.txt','r'),1):
    count +=1
    print(index,line)
print(count)
'''

for line in (open('ConfPython.txt','r')).readlines():
    print(line)


'''
data = []
    data.append(('预约码', '车牌号码', '进校时间段', '出校时间段', '进校校区',))
    for i in car_orders:
        data.append((i.order_number, i.car_number, i.during_in_time, i.during_out_time, i.in_school))

    for i, row in enumerate(data):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
'''