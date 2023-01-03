#!/usr/bin/python3
from socket import TIPC_SRC_DROPPABLE
import requests
from bs4 import BeautifulSoup



url = "https://www.imdb.com/chart/top"
site = requests.get(url)
doc = BeautifulSoup(site.text, 'html.parser')
table = doc.find('tbody', class_='lister-list').find_all('tr')

for movie in table:
    name = movie.find('td', class_='titleColumn').find('a')
    rating =movie.find('td', class_='ratingColumn imdbRating').find('strong')
    year = movie.find('td', class_='titleColumn').find('span')
    print("Movie: ",name.string)
    print("Rating: ",rating.string)
    print("Year: ",year.string)
    print("================================")


print("Procces Done.. ")

