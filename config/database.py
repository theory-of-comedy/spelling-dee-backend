import certifi
from pymongo import MongoClient
from config.config import get_settings

mongo_uri = get_settings().mongo_uri

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())

db = client["spelling-dee"]

collection_name = db["spelling-dee-collection"]
