import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3441652882'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

file = open('page.text', mode='w', encoding='utf-8')
file.write(soup.prettify())

prettyHTML = soup.prettify()
print(prettyHTML)
