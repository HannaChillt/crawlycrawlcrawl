from bs4 import BeautifulSoup
import requests
import pymongo
import os
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger()

mongo_host = os.environ.get("MONGO_SVC", "mongo") # mongo = service
mongo_port = 27017
# myclient = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}/?authSource=admin')
# log.debug("connected to db")
# mongodb = myclient["gruenderfounder_database"]
# mongodb.drop_collection('sponsorships')
# sponsorships_col = mongodb['sponsorships']
# print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

quelle = requests.get('https://www.exist.de/DE/Programm/Exist-Gruenderstipendium/Projektantrag/inhalt.html')
soup = BeautifulSoup(quelle.content, 'lxml')

fristenueberschrift = "Antragsfristen"
frist = soup.find('h2', text='Antragsfristen').find_next_sibling().text
insert_fristen = {"datum": frist, "info": "", "ueberschrift": fristenueberschrift}

searchfrist = soup.find_all('h2')
for h in searchfrist:
    if 'Antragsfristen' in h:
        fristenheading = h

schlagworte = ["Gründung", "exist"]
insert_sponsorship = {"name": "EXIST-Gründerstipendium",
                      "daten": insert_fristen,
                      "quelle": "https://www.exist.de/DE/Programm/Exist-Gruenderstipendium/Projektantrag/inhalt.html",
                      "info": "https://www.exist.de/DE/Programm/Exist-Gruenderstipendium/inhalt.html;jsessionid=67B51B5C2887B0BB5EEE6781AA5EED6D",
                      "schlagworte": schlagworte}

# name EXIST-Gründerstipendium
# termine
#   datum, info, ueberschrift
# quelle https://www.exist.de/DE/Programm/Exist-Gruenderstipendium/Projektantrag/inhalt.html
# info https://www.exist.de/DE/Programm/Exist-Gruenderstipendium/Konditionen/inhalt.html;jsessionid=AC5CBCC7EE53C86A003C3133F5503833
# schlagworte