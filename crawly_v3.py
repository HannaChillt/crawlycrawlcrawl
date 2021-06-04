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


source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('div', class_='gcms_text')  # ich kann nur nach content suchen, nicht nach os-content
print(len(search1))

trs = []
for div in search1:
    for tr in div.find_all('tr'):
        trs.append(tr.text.strip().split('\n'))

print(f'{trs}\n')

einzeltermine = re.split(r'\n+', search1[0].text)  # einzeltermine enthaelt nur einen Eintrag


valids = []
''''
for termin in einzeltermine:
    print(termin)
    if "Ort wird bekannt gegeben" not in termin:
        valids.append(termin)

for g in valids:
    print(g)
'''

pattern = re.compile(r"\d{2}\.\s[a-zA-ZäÄ]+\s\d{4}")

''''
while search1:
    for entry in search1:
        #print(entry)
        if pattern.findall(entry):
            print("hello")
            #print(search1.pop(entry.text.strip()))
'''''



#while search1:
    #data[search1.pop().text] = search1.pop().text
# print(f'laenge: {len(data)}')

#for i in data.keys():
    #print()
    #print(i + ', ' + data.get(i))

#termine1 = []
#keywords1 = []
#stipendium1 = Stipendium(1, termine1, "quelleeintragen", "infoeintragen", keywords1)



"""
an welcher Stelle sollen die Daten sortiert werden? sollen sie überhaupt sortiert werden?
als was sollen die Daten am Ende verpackt werden? json?
utf-8 encoding!!
"""
