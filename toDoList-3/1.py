from Tkinter import *

# self.label
root = Tk()
v = StringVar(value='type in your list')
class Item:
	"""the object of item"""
	def __init__(self, content):
		self.content = content
		self.label = Label(root, text=content)
		self.label.grid()

		

def addItem(event):
	v1 = StringVar()
	content = v.get()
	item = Item(content)
	e.delete(0, END)

e = Entry(root, textvariable=v)
e.bind("<Return>", addItem)
e.grid(row=1, column=0)



root.mainloop()