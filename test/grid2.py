from Tkinter import Button, Frame, Tk


class myButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, command=self.hideShowButton,
                        ** kwargs)
        self.visible = True

    def hideShowButton(self):
        self.visible = False
        self.pack_forget()

window = Tk()
frame = Frame(window)
frame.pack()
b1 = myButton(window, text="b1")
b1.pack()
b2 = myButton(window, text="b2")
b2.pack()
b3 = myButton(window, text="b3")
b3.pack()
window.wait_window(window)
print "At the end of the run b1 was %s, b2 was %s, b3 was %s" % (str(b1.visible), str(b2.visible), str(b3.visible))