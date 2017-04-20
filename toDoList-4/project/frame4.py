from Tkinter import *
import time
import ConfigParser
import os
import tkMessageBox
config = ConfigParser.RawConfigParser()

# Read the configration if it exists
# Create it if it does not exit
path = os.path.dirname(__file__)
configPath = path + '/myconfig.cfg'
check = os.path.exists(configPath)
if check == True:
    config.read('myconfig.cfg')

else:
    config.add_section('homework')
    config.add_section('programming')

TITLE_FONT = ("Consolas", 18, "bold")

class MyToDo(Tk):
    def __init__(self):
        Tk.__init__(self)

        m = Menu(self)
        self.config(menu=m)
        m.add_command(label='Clock', command=self.digitalClock)
        m.add_command(label='About', command=self.about)

        container =Frame(self)
        container.grid(row=1, column=2, rowspan=4)

        self.frames = {}
        for F in (Start , Homework, Programming):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nesw')

        self.show_frame("Start")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def digitalClock(self):
        def tick():
            time2 = time.strftime('%H:%M:%S')
            clock.config(text=time2)
            clock.after(200, tick)

        top = Toplevel()
        clock = Label(top, font=('times', 20, 'bold'), bg='green')
        clock.grid()
        tick()

    def about(self):
        top = Toplevel()
        message1 = 'Made by Zhang Qiaolun.'
        message2 = 'Contact Me: zhql0907@outlook.com'
        label1 = Label(top, text=message1)
        label2 = Label(top, text=message2)

        label1.grid()
        label2.grid()

class Start(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Do It Now Or Never", font=TITLE_FONT)
        label.grid()

        button1 = Button(self, text="Homework",
                            command=lambda: controller.show_frame("Homework"))
        button2 = Button(self, text="Programming",
                            command=lambda: controller.show_frame("Programming"))
        button1.grid()
        button2.grid()

class Homework(Frame):
     def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        frame = Frame(self)
        frame.grid(row=0, column=0)

        label1 = Label(frame, text="Homework", font=TITLE_FONT)
        label1.grid(row=0, column=0, sticky=W+E+N+S)

        button1 = Button(frame, text="Go to the start page",
                           command=lambda: controller.show_frame("Start"))
        button1.grid(row=0, column=0, sticky=W+E+N+S)


        v =StringVar(frame, value='Type in with number')

        e = Entry(frame, textvariable=v)
        e.bind("<Return>",lambda event :self.addItem(event, v, e, frame))
        e.grid(row=1, column=0)
        self.initItem(frame)

     def addItem(self, event, v, e, frame):
        content = v.get()
        item = Item(content, frame, 'homework')
        e.delete(0, END)

     def initItem(self, frame):
         savedItems = config.options('homework')
         for i in range(len(savedItems)):
             item = Item(savedItems[i], frame, 'homework')

class Programming(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        frame = Frame(self)
        frame.grid(row=0, column=0)

        label1 = Label(frame, text="Programming", font=TITLE_FONT)
        label1.grid(row=0, column=0, sticky=W+E+N+S)

        button1 = Button(frame, text="Go to the start page",
                           command=lambda: controller.show_frame("Start"))
        button1.grid(row=0, column=0, sticky=W+E+N+S)


        v =StringVar(frame, value='Type in with number')

        e = Entry(frame, textvariable=v)
        e.bind("<Return>",lambda event :self.addItem(event, v, e, frame))
        e.grid(row=1, column=0)
        self.initItem(frame)

    def initItem(self, frame):
        savedItems = config.options('programming')
        for i in range(len(savedItems)):
            item = Item(savedItems[i], frame, 'programming')


    def addItem(self, event, v, e, frame):
        content = v.get()
        item = Item(content, frame, 'programming')
        e.delete(0, END)

class Item:

    """the object of item"""
    def __init__(self, content, master, category):
        self.content = content
        self.category = category
        self.label1 = Label(master, text=content)
        self.label1.bind("<Button-1>", lambda event: self.changeContent(event, master))
        self.label1.bind("<Button-2>", lambda event: self.deleteItem(event, self.label1))
        self.label1.grid(column=0)
        config.set(self.category, self.content)
        saveConfig()

    def changeContent(self, event, master):

        top = Toplevel()
        v1 = StringVar()

        def returnContent(event, v1, label):
            content1 = v1.get()
            config.remove_option(self.category, self.content)
            self.content = content1
            label.config(text=content1)
            config.set(self.category, content1)
            saveConfig()
        e = Entry(top, textvariable=v1)
        e.bind("<Return>", lambda event: returnContent(event, v1, self.label1))
        e.grid()

    def deleteItem(self, event, label):
        # delete label(how to delete a widget)
        config.remove_option(self.category, self.content)
        saveConfig()
        label.grid_remove()

def saveConfig():
    with open('myconfig.cfg', 'wb') as configfile:
            config.write(configfile)

if __name__ == '__main__':
    app = MyToDo()
    app.mainloop()