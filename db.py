from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://test:pass@5117presentation.2d0ro.mongodb.net/5117Presentation?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('5117Presentation')
coll = pymongo.collection.Collection(db, 'info')
