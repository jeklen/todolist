#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 19:13:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import Tkinter as tk

TITLE_FONT = ("Consolas", 18, "bold")
CONTENT_FONT = ("Consolas", 10, "normal")

class Login(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		label1 = Label(self, text="User Name:")
		label2 = Label(self, text="Password:")
	
	# need to use destroy to remove all the wigits
	# if the password is correct	
	def checkPassword(self):
		getInfo()
		if check == True:
			
			

	def setUser(self):

	def resetUser(self):					







root = Tk()
label1 = Label(root, text="User Name:")
label2 = Label(root, text="Password:")
Label1.grid(row=0, sticky=W)
Label2.grid(row=1, sticky=W)
