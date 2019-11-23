import pymongo
import Config

client = pymongo.MongoClient(Config.db['connection_string'])
db = client[Config.db['database']]
workstations = db['workstations']

class Insert:
	def workstations(self, input_submit):
		if input_submit is None:
			print("Something went wrong")
		else:
			x = workstations.insert_one(input_submit)
			print(input_submit)
class Get:
	def first_entry(self, workstations):
		pass
for x in workstations.find():
	print(x)