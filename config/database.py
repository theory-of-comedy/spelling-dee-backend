import certifi
from pymongo import MongoClient

mongo_uri = "mongodb+srv://Bourbxn:Boss2546@spelling-dee.v2ekfip.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())

db = client["spelling-dee"]

collection_name = db["spelling-dee-collection"]
