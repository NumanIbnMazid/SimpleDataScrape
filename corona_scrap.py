import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')

columns = [
    'Country', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths',
    'Total Recovered', 'Active Cases', 'Critical'
]

list = soup.find('tbody')
# print(list)
trs = list.find_all('tr')
item_list = []

# 8
for counter, tr in enumerate(trs):
    tds = tr.find_all('td')
    items = []
    for c, td in enumerate(tds):
        if c <= 7:
            item = td.text.strip().replace('\n', '')
            items.append(item)
    item_list.append(items)

# print(item_list)

df = pd.DataFrame(
    item_list, columns=columns
)
df.to_csv('corona_data.csv', header=True, index=False)

