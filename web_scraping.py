#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

forp = doc.prettify()
print(forp) 

