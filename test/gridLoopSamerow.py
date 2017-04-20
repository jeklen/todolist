from Tkinter import *

#Input:
n = int(raw_input("Input whole positive number: "))
L = range(1,n+1)
k = n
m = n
#Try putting values for k and m which are less then n and you will see what   i need to get

#Moving:
def Move():
    #This i cant fill
    return k,m

#Program:
root = Tk()
for i in L:
    for j in L:
        frame = Frame(root)
        frame.grid(row = i,column = j)
        if i == int(k) and j == int(m):
            pass
        else:
            button = Button(frame, command = lambda: Move())
            button.pack()

root.mainloop()