import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JunhoKim:wnsgh-0609@cluster0.jisciv2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["software_engineering"]
collection = db["test"]

# post = {"_id":0, "name":"junho", "score": 90}
post1 = {"name":"YeHyun", "score": 80}
post2 = {"name":"JiYoung", "score": 70}

# x = collection.insert_one(post)
x = collection.insert_many([post1, post2])

results = collection.find({"name":"JiYoung"})
for results in results:
  print(results)
