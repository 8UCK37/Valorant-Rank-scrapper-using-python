import requests
from bs4 import BeautifulSoup


url = 'https://tracker.gg/valorant/profile/riot/CaRNaGePero%2369420/overview'
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parser')

div_element = soup.find('div', class_='rating-entry__rank-info')

value_text = div_element.find('div', class_='value').text.strip()

print(value_text)  


 


