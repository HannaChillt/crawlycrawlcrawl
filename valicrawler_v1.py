from bs4 import BeautifulSoup
import requests
import pymongo
import os

# host = os.environ.get("MONGO_SVC", "mongodb://admin:tMnfX7bNvjV6JGn@cluster0-shard-00-00.fypca.mongodb.net:27017,cluster0-shard-00-01.fypca.mongodb.net:27017,cluster0-shard-00-02.fypca.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-vm32vo-shard-0&authSource=admin&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")#"redis-svc", "localhost"
# database = os.environ.get("DATABASE_NAME", "gruenderfounder_database")
myclient = pymongo.MongoClient("mongodb://admin:tMnfX7bNvjV6JGn@cluster0-shard-00-00.fypca.mongodb.net:27017,cluster0-shard-00-01.fypca.mongodb.net:27017,cluster0-shard-00-02.fypca.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-vm32vo-shard-0&authSource=admin&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
mongodb = myclient["gruenderfounder_database"]
# mongodb.drop_collection('sponsorships')
sponsorships_col = mongodb['sponsorships']
print(f'names: {myclient.list_database_names()}, {mongodb.list_collection_names()}')

source = requests.get('https://www.validierungsfoerderung.de/foerderung/antragstellung-und-projektbegleitung')
soup = BeautifulSoup(source.content, 'lxml')

# name VIP+
# termine
#   datum, info, ueberschrift
# quelle
# info https://www.validierungsfoerderung.de/foerderung/vip-kompakt
# schlagworte