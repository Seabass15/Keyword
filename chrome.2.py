#import dependancies 

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#getting webpage
#options = Options()
#options = ChromeOptions()
options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
#options.headless = True 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
driver.get("https://www.indeed.com/jobs?q=cyber+security&l=Worcester%2C+MA&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&vjk=fdcae21a8820fca9")
#driver.quit()

#use bs4 to scan webpage

soup = BeautifulSoup(driver.page_source, 'html.parser') 
div = soup.findAll('div', {'class': 'jobsearch-BodyContainer'})

file = open('pages.txt', mode='w', encoding = 'utf-8')
file.write(div[0].get_text())
file.close()

