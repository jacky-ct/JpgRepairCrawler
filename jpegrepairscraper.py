from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://jpg.repair')
s = driver.find_element(By.XPATH, "//input[@type='file']")

img_path = os.getcwd() + '/images/'

s.send_keys(img_path + 'uncorrupted.jpg')

sleep(15)
print("1")

try:
    print("2")
    driver.find_element(By.XPATH, "//a[@onclick='checkFullDownload($mUserToken)']").click()

except NoSuchElementException:
    driver.find_element(By.XPATH, "//input[@multiple='false']").send_keys(img_path + 'reference.jpg')
    print("3")

sleep(5)


