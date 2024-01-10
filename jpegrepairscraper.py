from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

img_path = os.getcwd() + '/images/'

#options = webdriver.ChromeOptions()
#prefs = {"download.default_directory" : img_path + "/restored/"}
#options.add_experimental_option("prefs",prefs)

#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(60)


for i, j in enumerate(os.listdir(img_path + "/corrupted/")):
    driver.get('https://jpg.repair')

    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(img_path + 'corrupted/' + j)

    # This is an element that appears on all pages after the fixing page so we can identify when
    # fixing has finished with implicit wait
    driver.find_element(By.XPATH, "//div[@id='removetask']")
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.XPATH, "//a[@onclick='checkFullDownload($mUserToken)']").click()
        driver.implicitly_wait(60)


    except NoSuchElementException:
        driver.find_element(By.XPATH, "//input[@style='font-size: 50px; opacity: 0; position: absolute; right: -3px; top: -3px; z-index: 999;']").send_keys(img_path + 'reference.jpg')
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, "//a[@onclick='checkFullDownload($mUserToken)']").click()

    sleep(3)

    if i + 1 == len(os.listdir(img_path + "/corrupted/")):
        sleep(15)

input("Image decorruption successful, press any key to close")