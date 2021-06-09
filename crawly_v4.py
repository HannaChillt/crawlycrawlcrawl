from bs4 import BeautifulSoup
import requests
import re
import pymongo

myclient = pymongo.MongoClient("mongodb://admin:tMnfX7bNvjV6JGn@cluster0-shard-00-00.fypca.mongodb.net:27017,cluster0-shard-00-01.fypca.mongodb.net:27017,cluster0-shard-00-02.fypca.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-vm32vo-shard-0&authSource=admin&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
mongodb = myclient["gruenderfounder_database"]
# mongodb.drop_collection('sponsorships')
sponsorships_col = mongodb['sponsorships']
print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

source = requests.get('https://gruendungsstipendium-sh.de/de/termine')
soup = BeautifulSoup(source.content, 'lxml')

search1 = soup.find_all('div', class_='gcms_text')

trs = []
headings = []
for div in search1:
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
        insert_dates.append({'date': valids[counter][0], 'info': valids[counter][1], 'heading': headings[0]})
    if 4 <= counter < 8:
        insert_dates.append({'date': valids[counter][0], 'info': valids[counter][1], 'heading': headings[1]})
    if 8 <= counter < 12:
        insert_dates.append({'date': valids[counter][0], 'info': valids[counter][1], 'heading': headings[2]})
    counter += 1

keywords = ['Gründerstipendium', 'Geld']
insert_sponsorship = {'name': 'Gründungsstipendium', 'dates': insert_dates, 'source': 'https://gruendungsstipendium-sh.de/de/termine', 'info': 'https://gruendungsstipendium-sh.de/', 'keywords': keywords}
sponsorship_result = sponsorships_col.insert_one(insert_sponsorship)
