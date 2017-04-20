from Tkinter import *   

TITLE_FONT = ("Consolas", 18, "bold")

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
        label = Label(self, text="Homework", font=TITLE_FONT)
        label.grid(row=0, column=0, sticky=W+E+N+S)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("DoItNowOrNever"))
        button.grid(row=1, column=0, sticky=W+E+N+S)


class Programming(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Programming", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("DoItNowOrNever"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
