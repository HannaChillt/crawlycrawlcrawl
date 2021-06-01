from bs4 import BeautifulSoup
import requests
import json
import re

class Stipendium:
    def __init__(self, id, termine, quelle, info, keywords):
        self.id = id
        self.termine = termine
        self.quelle = quelle
        self.info = info
        self.keywords = keywords

class Termin:
    def __init__(self, id, datum, ueberschrift):
        self.id = id
        self.datum = datum
        self.ueberschrift = ueberschrift

# Funktion schreiben, der man die url gibt, dann kann für jede url die Funktion einfach aufgerufen werden und alles laeuft

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

termine1 = []
keywords1 = []
stipendium1 = Stipendium(1, termine1, "quelleeintragen", "infoeintragen", keywords1)



"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""
