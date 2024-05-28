from flask import Flask, request, jsonify
from pymongo import MongoClient

from bson.objectid import ObjectId
app = Flask(__name__)

cluster = MongoClient("mongodb+srv://JunhoKim:wnsgh-0609@cluster0.jisciv2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["software_engineering"]
collection = db["test"]

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/score', methods=['GET'])
def get_all_document():
  output = []
  for s in collection.find():
    s["_id"] = str(s["_id"]) #id를 string으로 바꿔줘야만 출력이 가능하다
    output.append(
      {'_id': s['_id'], 'name': s['name'], 'score': s['score']})
    
    return jsonify({'result': output})
  
@app.route('/score/<id>', methods=['GET'])
def get_one_document(id):
  s = collection.fond_one({'_id': ObjectId(id)})
  if s:
    s["_id"] = str(s["_id"])
    output = {'_id': s['_id'], 'name': s['name'], 'score': s['score']}
  else:
    output = "No such id"
  return jsonify({'result': output})

@app.route('/score', methods=['POST'])
def add_document():
  name = request.json['name']
  score = request.json['score']

  document_id = collection.insert_one({'name': name, 'score': score}).inserted_id
  new_document = collection.find_one({'_id': document_id})
  output = {'name': new_document['name'], 'score': new_document['score']}

  print("new document added")
  print(document_id)
  return jsonify({'result': output})

@app.route('/score/<id>', methods=['DELETE'])
def delete_document(id):
  s = collection.find_one({'_id': ObjectId(id)})
  if s:
    collection.delete_one({'_id': ObjectId(id)})
    return 'delete complete'
  else:
    output = "No such id"

  