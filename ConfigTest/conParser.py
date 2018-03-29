from configparser import ConfigParser
import re

'''

CONFIGFILE = "ConfPython.txt"
config=ConfigParser()
config.read(CONFIGFILE)

print(config.get('message','greeting'))

radius=float(input(config.get('message','question')+''))
print(type(radius))
print(config.get('message','result_message'))
print(type(config.getfloat('numbers','pi')))
print(config.getfloat('numbers','pi')*radius**2)
'''


ss='<source src="http://static.sfdict.com/audio/L01/L0123000.mp3" type="audio/mpeg">'
sdata=re.search('^<source src=("http://.*.mp3") type="audio/mpeg">',ss)
print(sdata.group(1))

