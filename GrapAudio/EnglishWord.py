from urllib import request
import re
import os
from sys import argv
'''
useage:
python EnglishWord.py deliberate rumor XXX

'''

def callbackProcess(a,b,c):
    '''
    :param a: Already downloaded data block
    :param b: the sizeof data
    :param c: the size of downloading file
    :return:
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%% %per')

words=[]
#words=['lawsuit','procrastinate','liquidate','negotiate','mattress','drapes','propaganda','drape','shelve']#,'mixed bag']
#url looks like: http://www.dictionary.com/browse/liquidate?s=t
url_root='http://www.dictionary.com/browse/'
dir = os.path.abspath('.')
Eng_words_dir='H:\Luo_Projects_Resources\dictionary_2018'
for iPos in range(1,len(argv)):
    words.append(argv[iPos])

for word in words:
    ss=url_root+word+"?s=t"
    print(ss)
    wdata=request.urlopen(ss)
    sdata=wdata.read().decode()
    print(type(sdata))
    audiofile=re.search('.*<source src="(http://.*.mp3)" type="audio/mpeg">.*',sdata)
    filepath=audiofile.group(1)
    print(filepath)
    work_path = os.path.join(Eng_words_dir, word+'.mp3')
    request.urlretrieve(filepath,work_path)
print("Downloading finished")
print("Please get the audio file from %s" %Eng_words_dir)



