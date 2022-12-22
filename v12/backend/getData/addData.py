from pymongo import MongoClient
from scraping import getDolar,getUf,getTemp,getGame
import time

#conexion a mongodb con user y pass
MONGO_URI = "mongodb://mongodb:27017/"
client = MongoClient(MONGO_URI,username="root",password="example")
db = client["db"]

start_time = str(time.time())

temperature = getTemp()
var = {'id': start_time, 'temp': temperature}
db['temperature'].insert_one(var)
'''
dollar = getDolar()
var = {'id': start_time, 'temp': dollar}
db['dollar'].insert_one(var)

uf = getUf()
var = {'id': start_time, 'temp': uf}
db['uf'].insert_one(var)

game = getGame()
var = {'id': start_time, 'temp': game}
db['game'].insert_one(var)
'''