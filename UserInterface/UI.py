from tkinter import Tk, Button
from UserInterface.Widgets import InputBox
import Data.DB as DB

class MainWindow:
	def __init__(self):
		self.master = Tk(className = "Asset Manager") # Creates Window with title
		#inputbox = Widgets.InputBox()

		#need to add a loop
		self.computer_name = InputBox(self.master, "Computer Name")
		self.computer_name.process()
		self.purchase_date = InputBox(self.master, "Purchase Date")
		self.purchase_date.process()

		self.submit_btn = Button(self.master, text = "Submit", command = self.submit)
		self.submit_btn.pack() 

	#Whilst pressing the Submit button. need to add a loop
	def submit(self):
		self.dbinsert = DB.Insert()
		self.dbinsert.workstations(self.computer_name.submit_input(), self.purchase_date.submit_input())
	
	#creates the main loop
	def start(self):
		self.master.mainloop()