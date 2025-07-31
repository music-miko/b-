from pymongo import MongoClient
from config import MONGO_URL

db = MongoClient(MONGO_URL).sarvesh_bot

def get_user(user_id):
    user = db.users.find_one({"_id": user_id})
    if not user:
        db.users.insert_one({"_id": user_id, "balance": 0, "orders": []})
        user = db.users.find_one({"_id": user_id})
    return user

def add_order(user_id, item):
    db.users.update_one({"_id": user_id}, {"$push": {"orders": item}})

def decrease_balance(user_id, amount):
    db.users.update_one({"_id": user_id}, {"$inc": {"balance": -amount}})