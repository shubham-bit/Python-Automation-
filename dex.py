from selenium import webdriver
from time import sleep
import os 

#Intialize Driver
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('https://en.wikipedia.org/wiki/main_page')
sleep(1)

#Input Data. #Send_keys function will type coronavirus. However, it can be anything. 
driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div/form/div/input[1]').send_keys('coronavirus')


#click on search button
driver.find_element_by_xpath (
    "/html/body/div[5]/div[1]/div[2]/div/form/div/input[4]").click()
sleep(1)

#can remove if want automated page to stay. 
driver.quit()

