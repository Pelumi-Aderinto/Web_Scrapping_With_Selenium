from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

with open('Real_estate.csv', 'w') as file:
    file.write("realtor_name; Location; Phone_no \n")
    

driver=webdriver.Chrome()


driver.get('https://www.expertise.com/ny/nyc/real-estate-agents')

driver.maximize_window()
time.sleep(5)


for k in range(28):
    show_number=driver.find_element(By.XPATH, '//div[@class="ProviderCard_tablet-screen__B00pn"]/div/button/span[1]')
    show_number.click()
    time.sleep(10)


realtor_name=driver.find_elements(By.XPATH, '//a[@data-location="title"]')
Location=driver.find_elements(By.XPATH, '//div[@class="Address_address__y0bmZ"]/address')
Phone_no=driver.find_elements(By.XPATH, '//div[@class="ProviderCard_tablet-screen__B00pn"]/div/button')

with open('Real_estate.csv', 'a') as file:
    for i in range(len(realtor_name)):
        file.write(realtor_name[i].text + ";" + Location[i].text + ";" + Phone_no[i].text  + "\n")
file.close()
driver.close()