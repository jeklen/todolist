#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-20 10:43:14
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from Tkinter import *
import time

root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

def tick():
	global time1
	# get the current local time from the PC
	time2 = time.strftime('%H:%M:%S')
	# if the time string has changed, update
	if time2 != time1:
		time1 = time2
		clock.config(text=time2)
		# calls itself every 200 milliseconds 
		# to update the time as needed
	clock.after(200, tick)


tick()
root.mainloop()
