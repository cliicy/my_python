from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

import confInfo
import pprint


uri="mongodb://"+confInfo.server+':'+confInfo.port+'/'+confInfo.test_db
client = MongoClient(uri)
dbname = client.luotest
collection=dbname.email
#for item in collection.find():
#print(collection)

for value in collection.find({},{"yahoo":1,"_id":0}):
    for val in value.values():
        print(val)
        eAddres,ePassword =str(val).split(':')
        print(eAddres,ePassword)

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.yahoo.com/")
driver.find_element_by_id("uh-mail-link").click()
try:
    print(ctime())
    driver.find_element_by_id("login-username").clear()
    driver.find_element_by_id("login-username").send_keys(eAddres)
    driver.find_element_by_id("login-signin").click()

    driver.find_element_by_id("login-passwd").clear()
    driver.find_element_by_id("login-passwd").send_keys(ePassword)

    driver.find_element_by_id("login-signin").click()
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())



print("Will log in yahoo email")
