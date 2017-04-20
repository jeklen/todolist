#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-20 16:32:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from Tkinter import *

root = Tk()
v = StringVar()



		
def addItem(event):
	content = v.get()
	label = Label(root, text=content)
	label.grid()
	print type(label)
	e.delete(0, END)

e = Entry(root, textvariable=v)
e.bind("<Return>", addItem)
e.grid(row=1, column=0)



root.mainloop()
