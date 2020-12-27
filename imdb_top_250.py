import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://www.imdb.com/chart/top/"

res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')

# print(soup.prettify())

page_title = soup.find('div', class_='article').h3.text
# print(page_title)
# IMDb Charts

list = soup.find('tbody', class_='lister-list')
items = list.find_all('tr')

# print(items)

titles = []
ratings = []
movies_dict = {}

filename = f"{page_title}.csv"
csv_writer = csv.writer(open(filename, 'w'))

nested_list = []

for counter, item in enumerate(items):
    title = item.find('td', class_='titleColumn').text
    rating = item.find('td', class_='ratingColumn').text
    titles.append(title)
    ratings.append(rating)
    movies_dict[title] = rating
    csv_writer.writerow([title, rating])
    # prepare for pandas nested list
    nested_list.append([counter + 1, title, rating])

df = pd.DataFrame(nested_list, columns=['#', 'Movie', 'Rating'])
df.to_csv('pandas_imdb.csv', header=True, index=False)

texts = []
for key, value in movies_dict.items():
    key = key.strip().replace('\n', '')
    value = value.strip()
    texts.append("Movie: " + key + " | Rating: " + value)


with open('imdb.txt', 'w') as outfile:
    outfile.write('\n'.join(texts))
