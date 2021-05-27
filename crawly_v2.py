from bs4 import BeautifulSoup
import requests
import json
import re

source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('div', attrs={'class': 'os-content'})
# print(search1)

data = {}
while search1:
    data[search1.pop().text] = search1.pop().text.encode('utf-8')

for entry in data:
    print(entry)
    print()



"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""
