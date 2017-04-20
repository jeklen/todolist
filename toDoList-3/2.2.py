from Tkinter import *
# self.label
root = Tk()
v = StringVar()
class Item:
    """the object of item"""
    def __init__(self, content):
        self.content = content
        self.label1 = Label(root, text=content)
        self.label1.bind("<Button-1>", lambda event: self.changeContent(event, root))
        self.label1.bind("<Button-2>", lambda event: self.deleteItem(event, self.label1))
        self.label1.grid(column=0)

    def changeContent(self, event, root):

        top = Toplevel()
        v1 = StringVar()

        def returnContent(event, v1, label):
            content1 = v1.get()
            label.config(text=content1)
        e = Entry(top, textvariable=v1)
        e.bind("<Return>", lambda event: returnContent(event, v1, self.label1))
        e.grid()

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