from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

with open('job_scraping_multipe_pages.csv', 'w') as file:
    file.write("Job_title; Company; Salary; Location; Job_description \n")
    

driver=webdriver.Chrome()

# driver.get('https://www.jobsite.co.uk/')

driver.get('https://www.jobsite.co.uk/jobs/data-engineer/in-united-kingdom?radius=30') # The particular url I wish to scrap

driver.maximize_window()
time.sleep(5)

# //*[@id="ccmgt_explicit_accept"]/span

cookie= driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]/span') # Locate the button to accept cookies
try:
    cookie.click()
except:
    pass 

time.sleep(5)
# job_title=driver.find_element(By.ID, 'keywords')
# job_title.click()
# job_title.send_keys('Software Engineer')
# time.sleep(1)

# location=driver.find_element(By.ID, 'location')
# location.click()
# location.send_keys('Manchester')
# time.sleep(1)

# dropdown=driver.find_element(By.ID, 'Radius')
# radius=Select(dropdown)
# radius.select_by_visible_text('30 miles')
# time.sleep(1)

# search=driver.find_element(By.ID, 'search-button')
# search.click()
# time.sleep(50)

for k in range(5):
    titles=driver.find_elements(By.XPATH, '//div[@class="resultlist-dpthza"]')
    company=driver.find_elements(By.XPATH, '//div[@class="resultlist-1mjyynf"]')
    salary=driver.find_elements(By.XPATH, '//div[@class="resultlist-noiqwp"]/span')
    location=driver.find_elements(By.XPATH, '//div[@class="resultlist-5dwl9c"]')
    job_details=driver.find_elements(By.XPATH, '//div[@class="resultlist-1n63zbq"]')

    with open('job_scraping_multipe_pages.csv', 'a') as file:
        for i in range(len(titles)):
            file.write(titles[i].text + ";" + company[i].text + ";" + salary[i].text + ";" + location[i].text + ";"+
                      job_details[i].text + "\n")

        next=driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
        next.click()
        time.sleep(7)
    file.close()
driver.close()