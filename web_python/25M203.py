import time

d1={"destination":'Bankok',"time":'2018-0707',"travelers":'Lili'}

'''
for key in d1:
    print(d1[key])
    
output:
Bankok
2018-0707
Lili
'''

'''
for item in d1.items():
        print(item)
        
output:
('destination', 'Bankok')
('time', '2018-0707')
('travelers', 'Lili')
'''


'''
for item in d1.__iter__():
    print(item)

for value in d1.values():
    print(value)
'''

for i in range(1,10,2):
    print(i)

print(time.ctime(100))