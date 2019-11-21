from tkinter import Entry, Label, Frame, StringVar, Button

class InputBox:
	def __init__(self, master, input_name):
		self.master = master
		self.input_name = input_name
		self.input_frame = Frame(self.master)
		self.input_frame.pack()
		self.input_data = Label(self.input_frame, text=self.input_name)
		self.input_data.pack(side="left")
		self.input_data = Entry(self.input_frame)
		self.input_data.pack()

	def process(self):

		self.check_input() #Fills the box initially
		self.input_data.bind("<FocusIn>",lambda _:self.check_input("in"))
		self.input_data.bind("<FocusOut>",lambda _:self.check_input("out"))

		#return 	(str(self.input_data.get()))
		#if self.check_input(): return self.check_input()

	'''Both checks if the forms are correct and fills/removes default values
	Needs adding messages if form not correct'''
	def check_input(self, focus="none"):
		if self.input_data.get() == "": #Fills the forms with default values
			self.input_data.insert(0,self.input_name)
			return False
		elif (self.input_data.get() == self.input_name) and (focus == "in"): #Clears the default value when clicking
			self.input_data.delete('0', 'end')
			return False
		elif (self.input_data.get() == self.input_name): 
			return False
		else:
			return True

	#this can be improved and will exclude need for checking in DB
	def submit_input(self):
		if self.check_input():
			return self.input_data.get()