import pymongo

client = pymongo.MongoClient("mongodb+srv://assetmanagement:o4kiykWtD40eilcU@training-ljw1a.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client['assetmanagement']
collection = db['workstations']

class Insert:
	def workstations(self, computer_name, purchase_date):
		dictionary = {"computer_name": computer_name, "purchase_date": purchase_date}
		if computer_name is None or purchase_date is None:
			print("Something went wrong")
		else:
			x = collection.insert_one(dictionary)
			print(dictionary)

for x in collection.find():
	print(x)