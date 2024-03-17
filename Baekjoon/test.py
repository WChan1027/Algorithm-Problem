from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import os

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.chuing.net/charasys/dungeon_dev/'
# url = 'https://www.naver.com'
driver.get(url)

# driver.find_element_by_class('MyView-module__link_login___HpHMW').click()

driver.find_element(By.ID, 'log_id').send_keys('baewc')
driver.find_element(By.ID, 'log_pw').send_keys('951027')
driver.find_element(By.ID, 'log_pw').send_keys(Keys.ENTER)

arrow = driver.find_element(By.TAG_NAME, 'html')

while True:
    driver.implicitly_wait(1)
    arrow.send_keys(Keys.ARROW_DOWN)
    driver.implicitly_wait(1)
    arrow.send_keys(Keys.ADD)
    driver.implicitly_wait(1)

    if driver.find_element(By.ID, 'QuesImg'):
        img = driver.find_element(By.ID, 'QuesImg').get_attribute('src')
        response = requests.get(img)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        num = pytesseract.image_to_string(image)
        print('1', num)
        break