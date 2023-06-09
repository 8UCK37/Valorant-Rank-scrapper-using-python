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
        player_data['agentHours']=values[1]
        player_data['winPerWithTopG']=values[2]
        player_data['TopGKd']=values[3]
        player_data['TopGadr']=values[4]
        player_data['TopGacs']=values[5]
    return values

def extract_values_from_giant_stats(div):
    values = {}
    name_spans = div.find_all('span', class_='name')
    value_spans = div.find_all('span', class_='value')

    for name_span, value_span in zip(name_spans, value_spans):
        name = name_span.text.strip()
        value = value_span.text.strip()
        values[name] = value
    
    return values

def extract_giant_stats(giant_stats):
    
    stat_divs = giant_stats.find_all('div', class_='stat align-left giant expandable')
    for stat_div in stat_divs:
        values = extract_values_from_giant_stats(stat_div)
        player_data.update(values)




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

giant_statsDiv = soup.find('div', class_='giant-stats')
extract_giant_stats(giant_statsDiv)
print(player_data)  