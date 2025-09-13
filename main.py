from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Initialize WebDriver

#driver = webdriver.Chrome(executable_path=r'C:\chromedriver-win64\chromedriver.exe')
service = Service(r'C:\chromedriver-win64\chromedriver.exe')
# Go to a website
IP = int(input("Enter IP "))
ht = "https://"
IPHT = '"'+ht+IP+'"'
driver= webdriver.Chrome(service=service)
driver.get(IPHT)