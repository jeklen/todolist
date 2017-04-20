from Tkinter import *   

MY_FONT = ("Consolas", 18, "bold")

class SampleApp(Tk):

    def __init__(self):
        Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        startPage = StartPage(container, self)
        self.frame[startPage] = startPage
        startPage.grid(row=0, column=0, sticky='nsew')
        pageOne = PageOne(container, self)
        self.frame[pageOne] = pageOne
        pageOne.grid(row=0, column=0, sticky='nsew')
        pageTwo = PageOne(container, self)
        self.frame[pageTwo] = pageTwo
        pageTwo.grid(row=0, column=0, sticky='nsew')
        self.show_frame("startPage")
###########################################################
#  'instancemethod' object does not support item assignment
###########################################################



    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the start page", font=MY_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("pageOne"))
        button2 = Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("pageTwo"))
        button1.pack()
        button2.pack()


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 1", font=MY_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("startPage"))
        button.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2", font=MY_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("startPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
