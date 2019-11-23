import pymongo

client = pymongo.MongoClient("mongodb+srv://assetmanagement:o4kiykWtD40eilcU@training-ljw1a.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client['assetmanagement']
collection = db['workstations']

class Insert:
	def workstations(self, input_submit):
		if input_submit is None:
			print("Something went wrong")
		else:
			x = collection.insert_one(input_submit)
			print(input_submit)

for x in collection.find():
	print(x)