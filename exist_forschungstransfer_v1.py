from bs4 import BeautifulSoup
import requests
import pymongo
import os
import logging
import sys
import re

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger()

mongo_host = os.environ.get("MONGO_SVC", "mongo") # mongo = service
mongo_port = 27017
myclient = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}/?authSource=admin')
log.debug("connected to db")
#mongodb = myclient["gruenderfounder_database"]
#mongodb.drop_collection('sponsorships')
#sponsorships_col = mongodb['sponsorships']
#print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

quelle = requests.get('https://www.exist.de/DE/Programm/Exist-Forschungstransfer/Antrag-Foerderphase-I/inhalt.html')
soup = BeautifulSoup(quelle.content, 'lxml')

fristenueberschrift = soup.find('h1', class_='isFirstInSlot').text.strip()
frist = soup.find('div', class_='subhead').text.strip()
fristen = re.findall('\d+\.\s\D+\d+\.\s\S+', frist)

insert_fristen = []
insert_fristen.append({"datum": fristen[0], "info": "Einreichung von Projektskizzen", "ueberschrift": fristenueberschrift})
insert_fristen.append({"datum": fristen[1], "info": "Einreichung von Projektskizzen", "ueberschrift": fristenueberschrift})

schlagworte = ["Gründung", "exist", "Forschungstransfer"]
insert_sponsorship = {"name": "EXIST-Gründerstipendium",
                      "daten": insert_fristen,
                      "quelle": "https://www.exist.de/DE/Programm/Exist-Forschungstransfer/Antrag-Foerderphase-I/inhalt.html",
                      "info": "https://www.exist.de/DE/Programm/Exist-Forschungstransfer/inhalt.html;jsessionid=9AACF5E6A3BFC6E5723E2955650341AA",
                      "schlagworte": schlagworte}

# sponsorship_result = sponsorships_col.insert_one(insert_sponsorship)

# name EXIST-Forschungstransfer
# termine
#   datum, info, ueberschrift
# quelle https://www.exist.de/DE/Programm/Exist-Forschungstransfer/Antrag-Foerderphase-I/inhalt.html
# info https://www.exist.de/DE/Programm/Exist-Forschungstransfer/inhalt.html;jsessionid=9AACF5E6A3BFC6E5723E2955650341AA
# schlagworte

