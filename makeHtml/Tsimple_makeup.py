import sys,re
import fileinput


from MyUtil import *
#from util import *

#file = sys.stdin
#if len(sys.argv) >1:
#    file=sys.argv[1]

print('<html><head><title>MyHtml</title></head></html>')
title=True

for block in blocks(sys.stdin):
#    for block in blocks(fileinput.input(file)):
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

