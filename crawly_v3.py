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
    def __init__(self, id, datum, info, ueberschrift):
        self.id = id
        self.datum = datum
        self.info = info
        self.ueberschrift = ueberschrift


source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('div', class_='gcms_text')  # ich kann nur nach content suchen, nicht nach os-content

trs = []
for div in search1:
    for tr in div.find_all('tr'):
        trs.append(tr.text.strip().split('\n'))

valids = []
for e in trs:
    if 'Ort wird bekannt gegeben' not in e:
        valids.append(e)

print(f'{valids}\n')

termine1 = []
zaehler = 0
for v in valids:
    termin = Termin('id', valids[zaehler][0], valids[zaehler][1], 'ueberschrift')
    termine1.append(termin)
    zaehler += 1
keywords1 = ['Gründerstipendium', 'Geld']
stipendium1 = Stipendium(1, termine1, 'https://gruendungsstipendium-sh.de/de/termine', 'https://gruendungsstipendium-sh.de/', keywords1)
print(f'{stipendium1.info}, {stipendium1.quelle}')
for t in stipendium1.termine:
    print(f'{t.datum}, {t.info}')

# pattern = re.compile(r"\d{2}\.\s[a-zA-ZäÄ]+\s\d{4}")
"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""
