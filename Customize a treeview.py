#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-28 14:55:11
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

# 此小组件用于显示具有层次结构的项目。例如，可以以这种方式再现Windows资源管理器。一些漂亮的表也可以使用treeviewwidget 完成。
import tkinter as tk
from tkinter import ttk

#创建小部件
root = tk.Tk()
tree=ttk.Treeview(root, style="mystyle.Treeview")
#列的定义
#您可以在用户尝试拉伸时定义多少列，宽度和最小宽度。通过定义stretch=tk.NO，用户无法修改列的宽度。

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)
#标题的定义
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)
#插入一些行
# Level 1
#myfolder = tree.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
#tree.insert("", 2, "", text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
# Level 2
#tree.insert(myfolder, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
#tree.insert(myfolder, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
#tree.insert(myfolder, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))
# 如果您希望根据行使用不同的格式，可以使用tags：
tree.insert("", "end", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"),tags = ('odd',))
tree.insert("", "end", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"),tags = ('even',))
tree.insert("", "end", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"),tags = ('odd',))
# 然后，例如，背景颜色可以与标签相关联：
tree.tag_configure('odd', background='#E8E8E8')
tree.tag_configure('even', background='#DFDFDF')

tree.pack(side=tk.TOP,fill=tk.X)
root.mainloop()