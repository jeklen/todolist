from Tkinter import *

# self.label
root = Tk()
v = StringVar(root, value='Enter your todo')
class Item:
    """the object of item"""
    def __init__(self, content):
        self.content = content
        self.v = StringVar(value=self.content)
        self.entry = Entry(root, text=self.v)
        self.entry.bind("<Button-2>", lambda event: self.changeContent(event, root))
        self.entry.bind("<Button-1>", lambda event: self.deleteItem(event, self.entry))
        self.entry.grid(column=0)

    def changeContent(self, event, root):
        v1 = StringVar
        top = Toplevel()
        e = Entry(top, textvariable=v1)
        e.bind("<Return>", lambda event: self.returnContent(event, v1))
        e.grid()
        top.destroy()

    def returnContent(self, v1):
        content = v1.get()
        self.label1.config(text=content)

    def deleteItem(self, event, label):
        # delete label(how to delete a widget)
        label.grid_remove()

def addItem(event):
    content = v.get()
    item = Item(content)
    e.delete(0, END)

e = Entry(root, textvariable=v)
e.bind("<Return>", addItem)
e.grid(row=1, column=0)



root.mainloop()
