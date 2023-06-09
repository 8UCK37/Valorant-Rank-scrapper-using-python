import requests
from bs4 import BeautifulSoup

player_data={}
def extract_values_from_div(div):
    values = []
    inner_divs = div.find_all('div')

    if inner_divs:
        for inner_div in inner_divs:
            value = inner_div.get('set')
            if value:
                values.append(value)
    
    if values:
        player_data['topAgent']=values[0]
        player_data['hours']=values[1]
        player_data['winPer']=values[2]
        player_data['kd']=values[3]
        player_data['adr']=values[4]
        player_data['acs']=values[5]
    return values


url = 'https://tracker.gg/valorant/profile/riot/Ez4aCE%237365/overview'
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parser')

rankDiv = soup.find('div', class_='rating-entry__rank-info')
rank = rankDiv.find('div', class_='value').text.strip()

# print('rank: ',rank)  
player_data['rank']=rank


agentDiv = soup.find('div', class_='st-content__category')
matchesPlayed = agentDiv.find('div', class_='label')
timesPlayed=matchesPlayed.text.strip()
player_data['macthesPlayed']=timesPlayed


divs = soup.find_all('div', class_='st-content__item')

for div in divs:
    imageDiv=div.find('div',class_='image')
    img_tag = imageDiv.find('img')
    if img_tag:
        src_url = img_tag['src']
        # print(src_url)
        player_data['agentUrl']=src_url
    values = extract_values_from_div(div)
    break
print(player_data)  