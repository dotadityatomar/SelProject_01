import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# Initialize WebDriver

service = Service(r'C:\chromedriver-win64\chromedriver.exe')

# Go to a website


driver= webdriver.Chrome(service=service)
driver.implicitly_wait(4)
driver.get("https://automationexercise.com/")
driver.find_element(By.CLASS_NAME,"fa fa-angle-right").click()
time.sleep(10)

