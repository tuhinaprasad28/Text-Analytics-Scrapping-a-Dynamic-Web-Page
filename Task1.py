import requests
from bs4 import BeautifulSoup

URL = "http://yuhenghu.com/ids566.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

week=soup.find_all('tr')

for week_element in week:
   title=week_element.find('td',class_='week')
   topic=week_element.find('td',class_='content')
   print(title.text, end='\t')
   print(topic.text)