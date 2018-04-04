from urllib import request
import os


def test(a1):
    a1.clear()
    a1.extend([3,4])

if __name__ == '__main__':
    b = [1,2]
    test(b)
#    print(b)
    fobj=open('conn.txt','w')

    with request.urlopen('http://www.sqlite.org/about.html') as f:
        data=f.read()
        print('Status',f.status,f.reason)
     #   print('reason')
        for k,v in f.getheaders():
            print('%s: %s' %(k,v))
         #   fobj.write('%s: %s' %(k,v))
        print('Data',data.decode('utf-8'))
        fobj.write(data.decode('utf-8'))
        fobj.close()