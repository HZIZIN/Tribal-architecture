#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 18:05:02
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

from tkinter import *
from random_tk import *
from random import choice
from tkinter import messagebox
import random


def Rrelief():
    # 随机 光标 样式
    return choice([FLAT, RAISED, SUNKEN, GROOVE, RIDGE, SOLID])


class initial:

    def __init__(self):
        root = Tk()
        self.root = root
        root.title("时间之外的往事")
        root.overrideredirect(False)
        # root.geometry("300x200")
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", self.closewindows)

        # create a popup menu
        self.menu = Menu(root, activebackground=rcolor(),
                         activeborderwidth=rnumber(), activeforeground=rcolor(),
                         bg=rcolor(), bd=rnumber(), cursor=rcursor(),
                         disabledforeground=rcolor(), font="Arial", fg=rcolor(),
                         relief=Rrelief(), selectcolor=rcolor(), tearoff=1, title="同志 欢迎加入")
        self.menu.add_command(label="进入部落", command=self.home)

        # create a image
        self.imgbg = PhotoImage(
            file='..\\..\\Pictures\\Installation_package.png')
        self.label = Label(root, image=self.imgbg)
        self.label.pack()

        # attach popup to canvas
        self.label.bind("<Button-1>", self.popup)
        root.mainloop()

    # 窗口X按钮
    def closewindows(self):
        if messagebox.askokcancel(title='Tips', message='退出需要验证暗号\n是否继续?'):
            top = Toplevel(bg=rcolor(), bd=rnumber(), cursor=rcursor(),  # fg=rcolor(),
                           height=300, width=200, relief=Rrelief())
            top.title("请输入关闭密码")
            top.maxsize(1024, 900)
            top.minsize(10, 10)
            top.resizable(1, 1)
            closeInput = Entry(top, show=None)
            closeInput.pack(fill='both', expand=1)
            closeButton = Button(top, text='灵感来源 电子教室')
            closeButton.pack(fill='both', expand=1)
        else:
            self.root.destroy()

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def home(self):
        top = Toplevel(bg=rcolor(), bd=rnumber(),
                       cursor=rcursor(), height=rnumber(),
                       width=rnumber(), relief=Rrelief())
        top.title("时间之外的联盟")
        top.geometry("300x200")
        top.resizable(True, True)


def main():
    initial()


if __name__ == '__main__':
    main()
