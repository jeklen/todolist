#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-17 19:35:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

print "Path at terminal when executing this file"
print (os.getcwd() + "\n")

print "This file path, relative to get os.getcwd()"
type(__file__)
print (__file__ + "\n")

print "This file full path (following symlinks)"
full_path = os.path.realpath(__file__)
print type(full_path)
print (full_path + "\n")

print ("This file directory and name")
path, filename = os.path.split(full_path)
print (path + ' --> ' + filename + "\n")

print "This file directory only"
print (os.path.dirname(full_path))

