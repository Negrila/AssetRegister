class Hardware:
 
	def __init__(self, name, purchase_date, ram, ssd):
		self.name = name
		self.purchase_date = purchase_date
		self.ram = ram
		self.hdd = ssd

	def describe(self):
		return "{} was purchased in {}. It has {} RAM and a ssd".format(self.name, self.purchase_date, self.ram)

class Laptop(Hardware):

	def charger(self, power):
		return "{} laptop has a {}W charger".format(self.name, power)

Lenovo_E570 = Laptop("Lenovo E570", "13/11/2019", 8, True)

print(Lenovo_E570.describe())
print(Lenovo_E570.charger(20))