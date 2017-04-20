from Tkinter import *
import ConfigParser
import time
config = ConfigParser.RawConfigParser()
config.add_section('homework')
config.add_section('programming')
# self.label
root = Tk()
v = StringVar(root, value='Type in with a number')

class Window:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.grid(row=1, column=1)

        v = StringVar(self.frame, value='Type in with a number')
        e = Entry(self.frame, textvariable=v)
        e.bind("<Return>", self.addItem)
        e.grid(row=0, column=0)
    def addItem(self, event):
        content = v.get()
        item = Item(content)
        e.delete(0, END)
    def show(self):
        self.frame.tkraise()

class Item:
    """the object of item"""
    def __init__(self, content):
        self.content = content
        self.label1 = Label(root, text=content)
        self.label1.bind("<Button-1>", lambda event: self.changeContent(event, root))
        self.label1.bind("<Button-2>", lambda event: self.deleteItem(event, self.label1))
        self.label1.grid(column=0)
        contentSplit = self.content.split()
        config.set('homework', contentSplit[0], contentSplit[1:])

    def changeContent(self, event, root):

        top = Toplevel()
        v1 = StringVar()

        def returnContent(event, v1, label):
            content1 = v1.get()
            label.config(text=content1)
            contentSplit1 = content1
            config.set('homework', contentSplit1[0], contentSplit1[1])
        e = Entry(top, textvariable=v1)
        e.bind("<Return>", lambda event: returnContent(event, v1, self.label1))
        e.grid()

    def deleteItem(self, event, label):
        # delete label(how to delete a widget)
        label.grid_remove()

def saveData():
    with open('myconfig.cfg', 'wb') as configfile:
        config.write(configfile)

def digitalClock():
    def tick():
        time2 = time.strftime('%H:%M:%S')
        clock.config(text=time2)
        clock.after(200, tick)

    top = Toplevel()
    clock = Label(top, font=('times', 20, 'bold'), bg='green')
    clock.pack(fill=BOTH, expand=1)
    tick()

m = Menu(root)
root.config(menu=m)
m.add_command(label='Save', command=saveData)
m.add_command(label='Clock', command=digitalClock)

homework = Window(root)
programming = Window(root)
homeworkshift = Label(root, text='Homework')
programmingshift = Label(root, text='Programming')

homeworkshift.grid(row=2, column=0)
programmingshift.grid(row=3, column=0)

root.mainloop()