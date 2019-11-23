from tkinter import Tk, Button
from UserInterface.Widgets import InputBox
import Data.DB as DB

class MainWindow:
	def __init__(self):
		self.master = Tk(className = "Asset Manager") # Creates Window with title
		self.input_field = ['Computer Name', 'Purchase Date', 'Assigned User'] #Set the input fields
		self.input_value = []

		#Generates input fields
		for i in range(len(self.input_field)):
			self.input_value.append(InputBox(self.master, self.input_field[i]))
			self.input_value[i].process()
	
		self.submit_btn = Button(self.master, text = "Submit", command = self.submit)
		self.submit_btn.pack() 

	#Processes the submit button
	def submit(self):
		self.input_submit = {}

		for i in range(len(self.input_field)):
			self.input_submit[self.input_field[i]] = self.input_value[i].submit_input()
		self.dbinsert = DB.Insert()
		self.dbinsert.workstations(self.input_submit)
	
	#creates the main loop
	def start(self):
		self.master.mainloop()