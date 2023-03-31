import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#new try
#selenium.webdriver.chrome.webdriver.WebDriver(executable_path='chromedriver', port=0, options= selenium.webdriver.chrome.options.Options = None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=None, service= selenium.webdriver.chrome.service.Service = None, keep_alive=None)

#old try
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

service = Service(executable_path=r"C:\Users\sebk1\chromedriver_win32")
driver = webdriver.Chrome(service=service)

from webdriver_manager.chrome import ChromeDriverManager
 
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHROMEDRIVER_PATH= r"C:\Program Files\Google\Chrome\Application"
URL = "https://www.indeed.com/jobs?q=cyber+security&l=Worcester%2C+MA&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&vjk=fdcae21a8820fca9"

options = Options()
options.headless = True 
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options = options)

driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')

file = open('page.text', mode='w', encoding = 'utf-8')
file.write(soup.prettify())

soup = BeautifulSoup.BeautifulSoup('<html><body><div id="jobDescriptionText"> ... </div></body></html')
soup.find("div", {"id": "jobDescriptionText"})
#id="job-details"> ... </div>

html = """
<div id="id" class="class">

 text

</div>
"""
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', attrs={'class': 'class'})
print (type(div.text))
print (div.text)