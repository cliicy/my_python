from selenium import webdriver

#driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium3")
driver.find_element_by_id("su").click()
driver.quit()