#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Generator
import Constants
import Tkinter

def getEntry():
    return entry.get()

def generateAll():
    generator = Generator.Generator(Constants.TypeFeatureAll, getEntry())
    generator.execute()

def generateBuilder():
    generator = Generator.Generator(Constants.TypeBuilder, getEntry())
    generator.execute()

root = Tkinter.Tk()

entry = Tkinter.Entry(root)
buttonAll = Tkinter.Button(root, text="All", command= generateAll)
buttonBuilder = Tkinter.Button(root, text="Builder", command= generateBuilder)
entry.pack()
buttonAll.pack()

root.mainloop()