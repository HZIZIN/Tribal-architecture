#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-14 09:35:04
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import tkinter as tk
import Organization
from tkinter import ttk
# from Organization import position


# 设置show属性为 headings 即可隐藏首列。
# height 行
root = tk.Tk()
root.title("组织名单")
columns=("one", "two", "three", "four")
tree = ttk.Treeview(root, height=18, show="headings", columns=columns)
# tree = ttk.Treeview(root, show='headings')
# tree["columns"] = ("one", "two", "three")
tree.column("one", width=60)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("three", width=100)
tree.heading("one", text="职务")
tree.heading("two", text="代号")
tree.heading("three", text="称号")
tree.heading("four", text="入伙时间")
tree.insert("", 0, values=("首领", "负责人事变动的", "Headmen", "一  2018.09"))
tree.insert("", 1, values=("副首", "部落专门收兵的", "魔域", "一  2018.09"))
tree.insert("", 2, values=("副首", "部落对战管理员", "戏子", "二  2018.09"))
tree.insert("", 3, values=("副首", "部落联赛管理员", "那年秋风起", "三  2018.09"))
tree.insert("", 4, values=("元老", "部落升级贡献者", "锤石", "四  2018.09"))
tree.insert("", 5, values=("元老", "部落升级贡献者", "死神VS火影", "五  2018.09"))
tree.insert("", 6, values=("成员", "部落升级贡献者", "一个江湖", "六  2018.09"))
tree.insert("", 7, values=("成员", "部落升级贡献者", "白营村", "七  2018.09"))
tree.insert("", 8, values=("成员", "部落升级贡献者", "海绵宝宝", "八  2018.09"))
tree.pack(fill='both', expand=1)


def LeftMouseClickToRelease(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('单击选中了:', item_text[:])  # 输出所选行的'第一列的'值


def treeviewClick(event):  # 双击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('双击:', item_text[0])  # 输出所选行的第一列的值
        Organization.position()
        a = Organization.position.Job_change
        print(a)
        # item_text[0] = a 元组


tree.bind('<ButtonRelease-1>', LeftMouseClickToRelease)  # 绑定单击离开事件===========
tree.bind('<Double-3>', treeviewClick)  # 绑定双击离开事件===========


for col in columns:  # 给所有标题加（循环上边的“手工”）
    tree.heading(col, text=col,
        command=lambda _col=col: treeview_sort_column(tree, _col, False))


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
    # 重写标题，使之成为再点倒序的标题


root.mainloop()
