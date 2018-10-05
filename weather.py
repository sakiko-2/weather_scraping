import requests
from bs4 import BeautifulSoup

URL = 'https://www.nzherald.co.nz/weather-home/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')

auckland = soup.find('h3', text='Auckland').find_parent().find_previous_sibling()
high = auckland.find(class_='high').get_text()
low = auckland.find(class_='low').get_text()
weather = ''.join(auckland.find('img')['class']).capitalize()

print('Auckland')
print(weather)
print(high)
print(low)
