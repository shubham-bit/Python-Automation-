from selenium import webdriver
from time import sleep
import os 


driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('https://en.wikipedia.org/wiki/main_page')
sleep(1)