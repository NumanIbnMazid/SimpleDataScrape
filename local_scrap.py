import requests
from bs4 import  BeautifulSoup

with open('html/index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# page_title = soup.select('title')[0].getText()
# or
page_title = soup.title.text
print(page_title)
# Freelancer - Start Bootstrap Theme

footer = soup.find('footer', class_='text-muted')  # class_ Because class is a buit in attribute in python
album = soup.find('div', class_='album')
# item_title = soup.find('h4', class_='item-title')
# or
item_title = album.h4.text
item_description = album.p.text
print(item_title)
# Item 1 Title
print(item_description)
# Item 1 Description

print("\n Get Albums through for loop. \n")
titles = []
descriptions = []
for album in soup.find_all('div', class_='album-item'):
    item_title = album.h4.text
    item_description = album.p.text
    titles.append(item_title)
    descriptions.append(item_description)

print(titles)
print(descriptions)
# ['Item 1 Title', 'Item 2 Title', 'Item 3 Title', 'Item 4 Title', 'Item 5 Title', 'Item 6 Title', 'Item 7 Title', 'Item 8 Title', 'Item 9 Title']
# ['Item 1 Description', 'Item 2 Description', 'Item 3 Description', 'Item 4 Description', 'Item 5 Description', 'Item 6 Description', 'Item 7 Description', 'Item 8 Description', 'Item 9 Description']

