from Tkinter import *

TITLE_FONT = ("Consolas", 18, "bold")

# I can put another frame at the botton
class ToDoList(Tk):

    def __init__(self):
        Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.grid()

        self.frames = {}
        for F in (DoItNowOrNever, Homework, Programming):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("DoItNowOrNever")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class DoItNowOrNever(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Do It Now Or Never", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Homework",
                            command=lambda: controller.show_frame("Homework"))
        button2 = Button(self, text="Programming",
                            command=lambda: controller.show_frame("Programming"))
        button1.pack()
        button2.pack()


class Homework(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        frame1 = Frame(self)
        frame1.grid(row=0, column=0)

        label = Label(frame1, text="Homework", font=TITLE_FONT)
        label.grid(row=0, column=0, sticky=W+E+N+S)

        frame2 = Frame(self)
        frame2.grid(row=1, column=0)

        button1 = Button(frame2, text="Go to the start page",
                           command=lambda: controller.show_frame("DoItNowOrNever"))
        button1.grid(row=0, column=0, sticky=W+E+N+S)
        button2 = Button(frame2, text="New", command=self.getTask)
        button2.grid(row=1, column=0)


    def getTask(self):
        top = Toplevel()
        label1 = Label(top, text='task')
        entry1 = Entry(top)
        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        button1 = Button(frame2, text="Confirm", command=self.putTask)
        button1.grid(row=0, column=3)
        print entry1.get()
        return entry1.get()



    def putTask(self):
        getTask(self)


    #def saveTask(self):



class Programming(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Programming", font=TITLE_FONT)
        label.grid(row=0, column=0, sticky=W+E+N+S)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("DoItNowOrNever"))
        button.grid(row=1, column=0, sticky=W+E+N+S)

if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()