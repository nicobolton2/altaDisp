from pymongo import MongoClient
from scraping import getDolar,getUf,getTemp

#conexion a mongodb con user y pass
MONGO_URI = 'mongodb://mongodb:27017/'
client = MongoClient(MONGO_URI,username='root',password='example')
db = client['db']

temperatura = getTemp()
print(temperatura)
print(temperatura)

var = {'id': '1', 'temp': temperatura}
db['temperature'].insert_one(var)

print("PASOOOOOOOOOOOOOOO")
print("PASOOOOOOOOOOOOOOO")
