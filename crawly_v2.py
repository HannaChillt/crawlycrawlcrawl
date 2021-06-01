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

class Parameter:
    def __init__(self, url, htmlelem, lookfor):
        self.url = url
        self.htmlelem = htmlelem
        self.lookfor = lookfor


suche1 = Parameter('https://gruendungsstipendium-sh.de/de/termine', '\'div\'', 'class_=\'content\'')
#print(suche1.lookfor)


# Funktion schreiben, der man die url gibt, dann kann für jede url die Funktion
# einfach aufgerufen werden und alles laeuft
# aus unbekannten gründen, funktioniert das hier nicht. die inhalte sind richtig im parameter,
# aber search ist leer, ich weiß nicht warum
def datensammeln(parameter):
    source = requests.get(parameter.url)
    soup = BeautifulSoup(source.content, 'lxml')

    print(parameter.url)
    print(parameter.htmlelem)
    print(parameter.lookfor)
    search = soup.find_all(parameter.htmlelem, parameter.lookfor)

    for entry in search:
        print("hello")
        print(entry.text.strip())


datensammeln(suche1)
''''
source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('div', class_='content') # ich kann nur nach content suchen, nicht nach os-content
#print(search1)
for entry in search1:
    print(entry.text.strip())
'''
data = {}
#while search1:
    #data[search1.pop().text] = search1.pop().text
# print(f'laenge: {len(data)}')

#for i in data.keys():
    #print()
    #print(i + ', ' + data.get(i))

termine1 = []
keywords1 = []
stipendium1 = Stipendium(1, termine1, "quelleeintragen", "infoeintragen", keywords1)



"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""
