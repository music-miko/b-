from pymongo import MongoClient
from config import MONGO_URL

db = MongoClient(MONGO_URL).sarvesh_bot

def get_all_items():
    return list(db.stock.find())

def get_item(name):
    return db.stock.find_one({"name": name})

def decrement_item(name):
    db.stock.update_one({"name": name}, {"$inc": {"quantity": -1}})