#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 21:41:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
#quit() stops the TCL interpreter. This is in most cases what you want, 
#because your Tkinter-app will also stop. It can be a problem, if you e.g. 
#call your app from idle. idle is itself a Tkinker-app, 
#so if you call quit() in your app and the TCL interpreter gets terminated, idle will also terminate (or get confused ). 
#destroy() just terminates the mainloop and deletes all widgets. 
#So it seems to be safer if you call your app from another Tkinter app, or if you have multiple mainloops."

root = Tk()

app = Chat(master=root)

class Chat(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()                   # default place:side = "top"

	def room_pm(self):
		root = Tk()
		app = Room(master)