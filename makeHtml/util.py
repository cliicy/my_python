import fileinput
import sys,re


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
            yield ''.join(block).strip()
            block=[]


'''
file='tt.txt'
ln = lines(file)
print(type(ln))
bl=blocks(file)
print(type(bl))

for line in ln:
    print(line)
    
'''



'''
不用yield的做法：
print('<html><head><title>MyHtml</title></head></html>')
title=True
try:
    for block in (fileinput.input(sys.argv[1])):
        if block.strip():
            block=re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
            if title:
                print('<h1>')
                print(block)
                print('</h1>')
                title=False
            else:
                print('<p>')
                print(block)
                print('</p>')
    print('</body></html>')
finally:
    pass
#    print('done')
'''



