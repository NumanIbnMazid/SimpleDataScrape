import requests
import bs4

res = requests.get('https://www.python.org/')
print(type(res))
# <class 'requests.models.Response'>

# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')

print(type(soup))
# <class 'bs4.BeautifulSoup'>

title = soup.select('title')
print(title)
# [<title>Welcome to Python.org</title>]

print(title[0])
# <title>Welcome to Python.org</title>

print(title[0].getText())
# Welcome to Python.org