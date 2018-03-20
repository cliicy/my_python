import time
import re

def test():
    now_time = time.time()
    b='test string'
    m='runoooorunoob'
    obj=re.match('runoo.*b',m)
    if obj:
        print("obj.group() : ", obj.group())
        #print("obj.group(1) : ", obj.group(1))
        #print("obj.group(2) : ", obj.group(2))

    #sre=re.match('[\s\S]*',b)
    #sre=re.match('^[A-Za-z]+$',b)
    sre = re.match('.*', b)
    if sre:
        print("sre.group() : ", sre.group())
        #print("sre.group(1) : ", sre.group(1))
        #print("sre.group(2) : ", sre.group(2))
    print(sre)

    obj = re.search('[\S]+',b)
    if obj:
        print(obj.group())
        #print(obj.group(0))
        #print(obj.group(1))
    print(obj)

    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")


if __name__ == '__main__':
    test()