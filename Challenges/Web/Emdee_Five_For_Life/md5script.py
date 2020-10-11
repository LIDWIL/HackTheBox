from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import hashlib

url = 'http://134.122.109.72:31130' #Dependent on the IP and Port of the site given by HackTheBox
driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")
driver.get(url)

md5_sum = hashlib.md5()

tag = str(driver.find_element_by_xpath("/html/body/h3").get_attribute("innerHTML"))
print(tag)
md5_sum.update(tag.encode())

print(md5_sum.hexdigest())

md5input = driver.find_element(By.NAME, 'hash')
md5input.send_keys(md5_sum.hexdigest() + Keys.RETURN)
