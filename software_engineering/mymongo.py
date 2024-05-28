import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JunhoKim:wnsgh-0609@cluster0.jisciv2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["software_engineering"]
collection = db["test"]
post = {"_id":0, "name":"junho", "score": 90}
x = collection.insert_one(post)