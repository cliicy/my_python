from urllib import request
import logging

logging.basicConfig(level=logging.INFO, filename='mylog.txt')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0')
print(1/0)
logging.info('The division succeeded')
logging.info('Ending program')


'''
log=open('mylog.txt','w')
url='https://docs.python.org'
print('Today is Wed.Downloading file from URL %s' %url)>>log
text = request.urlopen(url).read()
print(text,'File successfully downloaded')>>log
'''