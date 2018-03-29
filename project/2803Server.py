import socket
from urllib import request
import re



webpage=request.urlopen('http://www.python.org')
text=webpage.read()
print(type(text))
ss=text.decode()
print(type(ss))
#text='<a href="/about/" title="" class="">About</a>'
m=re.search('<a href="([^"]+)" .*?>about</a>',ss,re.IGNORECASE)
print(m.group(1))
#print(m.group(1))



'''

s=socket.socket()
host=socket.gethostname()
port=1234
s.bind(host,port)

s.listen(5)
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send('Thank you for connection')
    c.close()

'''