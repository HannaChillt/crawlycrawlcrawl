from bs4 import BeautifulSoup
import requests
import json
import re

source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('td', attrs={'style': 'width: 49.65346534653465%;'}) # DAS GEHT <3

data = {}
while search1:
    data[search1.pop().text] = search1.pop().text

for i in data.keys():
    print()
    print(i + ', ' + data.get(i))
print(json.dumps(data, sort_keys=True))
print(len(data))

"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""

#for deadline in soup.find_all('a', class_='responsive_tables'):
    #print(deadline)
