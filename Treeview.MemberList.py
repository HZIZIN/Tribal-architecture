#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-14 09:35:04
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import tkinter as tk
from tkinter import ttk


# 设置show属性为 headings 即可隐藏首列。
# height 行
root = tk.Tk()
root.title("组织名单")
columns = ["zero", "one", "two", "three", "four", "five","six"]
headtext = ["排名", "职务", "头衔", "落网时间", "联赛", "竞赛", "组织内代号"]
tree = ttk.Treeview(root, height=18, show="headings", columns=columns)
# tree = ttk.Treeview(root, show='headings')
# tree["columns"] = ("one", "two", "three")
tree.column("zero", width=35)
tree.column("one", width=35)
tree.column("two", width=100)
tree.column("three", width=90)
tree.column("four", width=40)
tree.column("five", width=50)
tree.column("six", width=120)
'''
tree.heading("zero", text="排名")
tree.heading("one", text="职务")
tree.heading("two", text="称号")
tree.heading("three", text="入伙时间")
tree.heading("four", text="联赛状态")
tree.heading("five", text="代号")
'''
tree.insert("", 0, values= ('00', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "不败只是个神话"))
tree.insert("", 1, values= ('01', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "估计人不多吧"))
tree.insert("", 2, values= ('02', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "木匠"))
tree.insert("", 3, values= ('03', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "陈翔六点半"))
tree.insert("", 4, values= ('04', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "大香蕉"))
tree.insert("", 5, values= ('05', "成员", "部落对战管理员", "一  2018.09.00", "参战", "1 4000", "戏子"))
tree.insert("", 6, values= ('06', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "一個 &江湖"))
tree.insert("", 7, values= ('07', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "死神VS火影"))
tree.insert("", 8, values= ('08', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "阴阳之气"))
tree.insert("", 9, values= ('09', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "仗神打"))
tree.insert("", 10, values=('10', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "MKA马小少"))
tree.insert("", 11, values=('11', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "风云决"))
tree.insert("", 12, values=('12', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "未来的世界"))
tree.insert("", 13, values=('13', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "叶何"))
tree.insert("", 14, values=('14', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "屁多"))
tree.insert("", 15, values=('15', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "枫丹白露"))
tree.insert("", 16, values=('16', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "CimIJH"))
tree.insert("", 17, values=('17', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "锤石"))
tree.insert("", 18, values=('18', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "戏子"))
tree.insert("", 19, values=('19', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "残笑"))
tree.insert("", 20, values=('20', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "Headman"))
tree.insert("", 21, values=('21', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "Pop@逗鼻成"))
tree.insert("", 22, values=('22', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "纷争霸业"))
tree.insert("", 23, values=('23', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "战斗机中的精英"))
tree.insert("", 24, values=('24', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "此生逍遥天莫问"))
tree.insert("", 25, values=('25', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "打我的是**"))
tree.insert("", 26, values=('26', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "香榭丽舍"))
tree.insert("", 27, values=('27', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "风住尘香花已尽"))
tree.insert("", 28, values=('28', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "亚太"))
tree.insert("", 29, values=('29', "成员", "部落联赛管理员", "一  2018.10.00", "参战", "1 4000", "那年秋风起"))
tree.insert("", 30, values=('30', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "光明"))
tree.insert("", 31, values=('31', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "《快乐大本营》"))
tree.insert("", 32, values=('32', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "羽飘渺"))
tree.insert("", 33, values=('33', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "光速FLASH"))
tree.insert("", 34, values=('34', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "总有刁民想赢朕"))
tree.insert("", 35, values=('35', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "那剩下的一天"))
tree.insert("", 36, values=('36', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "先生"))
tree.insert("", 37, values=('37', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "海绵宝宝"))
tree.insert("", 38, values=('38', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "尤拉部落"))
tree.insert("", 39, values=('39', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "白营村"))
tree.insert("", 40, values=('40', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "西天皓月"))
tree.insert("", 41, values=('41', "成员", "部落升级贡献者", "一  2019.06.25", "参战", "1 4000", "的音开一"))
tree.insert("", 42, values=('42', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "IIII"))
tree.insert("", 43, values=('43', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "一个人"))
tree.insert("", 44, values=('44', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "愿你笑颜如"))
tree.insert("", 45, values=('45', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "NB宝贝宝贝"))
tree.insert("", 46, values=('46', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "朕的江山"))
tree.insert("", 47, values=('47', "成员", "部落升级贡献者", "一  2018.09.00", "参战", "1 4000", "离念2"))
tree.insert("", 48, values=('48', "成员", "部落升级贡献者", "一  2019.09.00", "参战", "1 4000", "死神"))
tree.insert("", 49, values=('49', "成员", "部落专门收兵的", "一  2018.09.00", "参战", "1 4000", "魔域源"))
tree.insert("", 50, values=['50', "成员", "部落升级贡献者", "一  2019.06.25", "参战", "1 4000", "GOD Robot"])
tree.pack(fill='both', expand=1)
def LeftMouseClickToRelease(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('单击选中了:', item_text[:])  # 输出所选行的'第一列的'值


def treeviewClick(event):  # 双击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('双击:', item_text[0])  # 输出所选行的第一列的值
    from Organization import position
    position()
    a = position.Job_change
    print(a)
    # item_text[0] = a 元组


tree.bind('<ButtonRelease-1>', LeftMouseClickToRelease)  # 绑定单击离开事件===========
tree.bind('<Double-3>', treeviewClick)  # 绑定双击离开事件===========

i = 0  # 索引修改标题
for col in columns:  # 给所有标题加（循环上边的“手工”）
    tree.heading(col, text=headtext[i],
        command=lambda _col=col: treeview_sort_column(tree, _col, False))
    i += 1


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
