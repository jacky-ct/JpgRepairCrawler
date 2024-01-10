import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

img_path = os.getcwd() + '/images/'

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
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH,
                            "//input[@style='font-size: 50px; opacity: 0; position: absolute; right: -3px; top: -3px; z-index: 999;']") \
                            .send_keys(img_path + 'reference.jpg')
        
        driver.find_element(By.XPATH, "//a[@onclick='checkFullDownload($mUserToken)']").click()

    os.remove(img_path + 'corrupted/' + j)
    sleep(3)
    print(f"Image no. {i + 1} downloaded")

    if i + 1 == len(os.listdir(img_path + "/corrupted/")):
        sleep(15)

input("\nImage decorruption successful, press any key to close")
