from bs4 import BeautifulSoup
import requests
import pymongo
import os
import logging
import sys

# host = os.environ.get("MONGO_SVC", "mongodb://admin:tMnfX7bNvjV6JGn@cluster0-shard-00-00.fypca.mongodb.net:27017,cluster0-shard-00-01.fypca.mongodb.net:27017,cluster0-shard-00-02.fypca.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-vm32vo-shard-0&authSource=admin&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")#"redis-svc", "localhost"
# database = os.environ.get("DATABASE_NAME", "gruenderfounder_database")
# myclient = pymongo.MongoClient("mongodb://admin:tMnfX7bNvjV6JGn@cluster0-shard-00-00.fypca.mongodb.net:27017,cluster0-shard-00-01.fypca.mongodb.net:27017,cluster0-shard-00-02.fypca.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-vm32vo-shard-0&authSource=admin&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger()

mongo_host = os.environ.get("MONGO_SVC", "mongo") # mongo = service
mongo_port = 27017
myclient = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}/?authSource=admin')
log.debug("connected to db")
mongodb = myclient["gruenderfounder_database"]
# mongodb.drop_collection('sponsorships')
stipendium_col = mongodb['sponsorships']
print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

quelle = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(quelle.content, 'lxml')

suche1 = soup.find_all('div', class_='gcms_text')

trs = []
headings = []
for div in suche1:
    for h2 in div.find_all('h2'):
        if 'Stipendiaten-Treffen' not in h2:
            headings.append(h2.text.strip())
    for tr in div.find_all('tr'):
        trs.append(tr.text.strip().split('\n'))

valids = []
for e in trs:
    if 'Ort wird bekannt gegeben' not in e:
        valids.append(e)

#print(f'{valids}\n')

insert_dates = []
counter = 0
for v in valids:
    if counter < 4:
        insert_dates.append({"datum": valids[counter][0], "info": valids[counter][1], "ueberschrift": headings[0]})
    if 4 <= counter < 8:
        insert_dates.append({"datum": valids[counter][0], "info": valids[counter][1], "ueberschrift": headings[1]})
    if 8 <= counter < 12:
        insert_dates.append({"datum": valids[counter][0], "info": valids[counter][1], "ueberschrift": headings[2]})
    counter += 1

schlagworte = ["Gründerstipendium", "Geld"]
insert_sponsorship = {"name": "Gründungsstipendium", "daten": insert_dates, "quelle": "https://gruendungsstipendium-sh.de/de/termine", "info": "https://gruendungsstipendium-sh.de/", "schlagworte": schlagworte}
sponsorship_result = stipendium_col.insert_one(insert_sponsorship)
log.debug("fed db")
