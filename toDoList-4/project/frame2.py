from Tkinter import *
import time
import ConfigParser
config = ConfigParser.RawConfigParser()
config.add_section('homework')
config.add_section('programming')

TITLE_FONT = ("Consolas", 18, "bold")

class MyToDo(Tk):
    def __init__(self):
        Tk.__init__(self)

        m = Menu(self)
        self.config(menu=m)
        m.add_command(label='Save', command=self.saveData)
        m.add_command(label='Clock', command=self.digitalClock)

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

    def saveData(self):
        with open('myconfig.cfg', 'wb') as configfile:
            config.write(configfile)
    def digitalClock(self):
        def tick():
            time2 = time.strftime('%H:%M:%S')
            clock.config(text=time2)
            clock.after(200, tick)

        top = Toplevel()
        clock = Label(top, font=('times', 20, 'bold'), bg='green')
        clock.pack(fill=BOTH, expand=1)
        tick()

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

     def addItem(self, event, v, e, frame):
        content = v.get()
        item = Item(content, frame)
        e.delete(0, END)

class Programming(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        frame = Frame(self)
        frame.grid(row=0, column=0)

        label = Label(self, text="Programming", font=TITLE_FONT)
        label.grid(row=0, column=0, sticky=W+E+N+S)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Start"))
        button.grid(row=1, column=0, sticky=W+E+N+S)

        v =StringVar(frame, value='Type in with number')

        e = Entry(frame, textvariable=v)
        e.bind("<Return>",lambda event :self.addItem(event, v, e))
        e.grid(row=1, column=0)

    def addItem(self, event, v, e):
        content = v.get()
        item = Item(content)
        e.delete(0, END)

class Item:

    """the object of item"""
    def __init__(self, content, master):
        self.content = content
        self.label1 = Label(master, text=content)
        self.label1.bind("<Button-1>", lambda event: self.changeContent(event, master))
        self.label1.bind("<Button-2>", lambda event: self.deleteItem(event, self.label1))
        self.label1.grid(column=0)
        contentSplit = self.content.split()
        config.set('homework', contentSplit[0], contentSplit[1:])

    def changeContent(self, event, master):

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

if __name__ == '__main__':
    app = MyToDo()
    app.mainloop()