from Tkinter import *
import time
import tkMessageBox

class Countdown:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()

        self.entry = Entry(frame, width=15)
        self.entry.grid(row=0, column=0)

        self.startButton = Button(frame, text='Start', command=self.start)
        self.startButton.grid(row=0, column=1)

        self.leaveButton =Button(frame, text='QUIT', fg='red', command=frame.quit)
        self.leaveButton.grid(row=0, column=2)

        self.label = Label(frame, width=30)
        self.label.grid()

    def start(self):
        text = self.entry.get().strip()
        if text != ''
            num = int(text)
            self.countTime(num)

    def countTime(self, minute):
        self.label.config(bg='yellow')
        self.label.config(font=('Consolas', 20, 'bold'))
        for k in range(minute, 0, -1):
            self.label['text'] = k
            root.update()
            time.sleep(60)

        self.label.config('bg=red')
        self.label.config('fg=white')

        self.label['text'] = 'Time up!'
        tkMessageBox.showinfo('Time up!', 'Time up!')


