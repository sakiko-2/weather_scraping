import requests
from bs4 import BeautifulSoup

URL = 'https://www.nzherald.co.nz/weather-home/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')

city = 'Auckland'
regional_data = soup.find('h3', text=city).find_parent().find_previous_sibling()
high = regional_data.find(class_='high').get_text()
low = regional_data.find(class_='low').get_text()
weather = ''.join(regional_data.find('img')['class']).capitalize()

print(city)
print(weather)
print(high)
print(low)
