import requests
from bs4 import BeautifulSoup
import time
import csv

r = requests.get("https://editorial.rottentomatoes.com/guide/movies-100-percent-score-rotten-tomatoes/")
r.raise_for_status()
soup = BeautifulSoup(r.content, 'html.parser')

title_element = soup.find("h1")
title = title_element.text.strip() if title_element else None
print(title)