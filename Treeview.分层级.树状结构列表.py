#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-14 09:00:38
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)#, show='headings')
tree["columns"] = ("one", "two", "thr")
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("thr", width=100)
tree.heading("one", text="职务")
tree.heading("two", text="代号")
tree.heading("thr", text="入伙时间")
tree.insert("", 0, values=("首领","Headmen", "一  2018.9"))
id1 = tree.insert("", 1, "dir2", text="副首领")
tree.insert(id1, "end", "dir3", values=("部落对战管理员", "戏子", "二  2018.9"))
tree.insert(id1, "end", "dir4", text="部落对战联赛管理", values=("那年秋风起", "三 2018.9"))
id2 = tree.insert("", 2, "dir5", text="长老")
tree.insert(id2, "end", "dir6", text="元老", values=("锤石", "一 2018.9"))
tree.insert(id2, "end", "dir7", text="元老", values=("死神VS火影", "一 2018.9"))
id3 = tree.insert("", 3, "dir8", text="成员")
tree.insert(id3, "end", "dir9", text="核心成员", values=("魔域", "一 2018.9"))
tree.pack(fill='both', expand=1)
root.mainloop()
