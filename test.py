#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-01 18:16:13
# @Author  : IOqbit (ioqbit@163.com)
# @Link    : https://hzizin.github.io/
# @Version : $Id$

from tkinter import *

from random_tk import *


def callback(event):
    '''显示当前鼠标坐标'''
    str_obj.set("X:%d\nY:%d" % (event.x, event.y))


def minimize():
    root.state("iconic")


def shutdown():
    root.destroy()


def popup(self, event):
    '''跟随鼠标位置显示菜单'''
    menu.post(event.x_root, event.y_root)


def donothing():
    pass


root = Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.title('屏幕检测')
root.geometry('{}x{}+{}+{}'.format(int(screenwidth / 1.2),
                                   int(screenheight / 1.5), 0, 0))
root.iconbitmap('..\\Documents\\Pictures\\Mozilla.ico')


menubar = Menu(root, selectcolor="light slate blue")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
# 在菜单中添加分隔线。

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
