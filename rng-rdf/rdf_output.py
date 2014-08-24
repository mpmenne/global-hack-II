from pymongo import MongoClient

prefix = "\n".join(["@prefix node:   <http://54.200.98.221:5000/api/v1/nodes#>", 
    "@prefix connection: <http://54.200.98.221:5000/api/v1/connections#>"])
print prefix


client = MongoClient('54.200.98.221', 27017)
db = client['maindb']

THRESH_HOLD = 10

data = db.connections.find({'score': {'$gt': THRESH_HOLD}}).sort("score")

for datum in data:
    entry = ""
    entry += "node:" + str(datum['primary_node_id']) + " "
    entry += "connection:" + datum['relationship'] + " "
    entry += "node:" + str(datum['related_node_id'])

    print entry

