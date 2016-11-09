#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Generator
import Constants
import Tkinter
import subprocess
import os


def getEntry():
    return entry.get()


def generateAll():
    generator = Generator.Generator(Constants.TypeFeatureAll, getEntry())
    generator.execute()


def generateBuilder():
    generator = Generator.Generator(Constants.TypeBuilder, getEntry())
    generator.execute()


def openExplore():
    subprocess.Popen(r'explorer /select,"./"')


root = Tkinter.Tk()
message = Tkinter.StringVar()
hintMes = Tkinter.Label(root, textvariable=message).pack()
message.set("Enter Name: ")

entry = Tkinter.Entry(root)
entry.pack()
buttonAll = Tkinter.Button(root, text="All", command=generateAll).pack()
buttonBuilder = Tkinter.Button(root, text="Builder", command=generateBuilder).pack()
buttonOpenExplore = Tkinter.Button(root, text="Open Folder", command=openExplore).pack()

root.mainloop()
