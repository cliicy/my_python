'''
line='\n'
str=line.strip()
print('a')
print(line)
'''
string=['string','always','moving','travel']


def lines(file):
    for line in file:
        yield line
        yield '\n'


def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
#            yield ''.join(block).strip()
#            print('finish blocks func')
            block=[]
#            print(block)


#for line in blocks(string):
#    print(line)

'''

def addlist(alist):
    for i in alist:
        yield i + 1
        print(str(i),'aa')

def addlist2(alist):
    for i in alist:
        i= i + 1


alist = [1, 2, 3, 4]
for x in addlist(alist):
    print(x)
    
'''

'''

def createGenerator():
    mylist=range(3)
    for i in mylist:
        yield i*i
        print(str(i),'a')


mygentor=createGenerator()
print(mygentor)
for i in mygentor:
    print(i)
'''


listStr = ['python', 'tab', '.com']
website = ''.join(listStr)
print(website)