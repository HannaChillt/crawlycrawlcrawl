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
# myclient = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}/?authSource=admin')
# log.debug("connected to db")
# mongodb = myclient["gruenderfounder_database"]
# mongodb.drop_collection('sponsorships')
# sponsorships_col = mongodb['sponsorships']
# print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

source = requests.get('https://www.exist.de/DE/Programm/Exist-Forschungstransfer/Antrag-Foerderphase-I/inhalt.html')
soup = BeautifulSoup(source.content, 'lxml')

fristenueberschrift = soup.find('h1', class_="isFirstInSlot").text.strip()
fristen = soup.find('div', class_="subhead").text.strip()

pattern = re.compile(r"\d+\.\s\D+\d+\.\s\S+")
einzelfristen = re.findall(pattern, fristen)
insert_fristen = []
insert_fristen.append({"date": einzelfristen[0], "info": "Einreichung von Projektskizzen", "heading": fristenueberschrift})
insert_fristen.append({"date": einzelfristen[1], "info": "Einreichung von Projektskizzen", "heading": fristenueberschrift})

keywords = ["Gründung", "exist", "Forschung"]
insert_sponsorship = {"name": "EXIST-Forschungstransfer",
                      "dates": insert_fristen,
                      "source": "https://www.exist.de/DE/Programm/Exist-Forschungstransfer/Antrag-Foerderphase-I/inhalt.html",
                      "info": "https://www.exist.de/DE/Programm/Exist-Forschungstransfer/inhalt.html",
                      "keywords": keywords}

# sponsorship_result = sponsorships_col.insert_one(insert_sponsorship)