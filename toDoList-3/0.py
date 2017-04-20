#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-23 21:41:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from Tkinter import *

root = Tk()
v = StringVar(root, value='default text')
e = Entry(root, textvariable=v)
e.pack()
root.mainloop()
