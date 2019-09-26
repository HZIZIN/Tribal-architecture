#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 15:26:27
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : 2.0

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

position_select = ''
# '全局变量 闭包 局部变量' 混乱，统一使用全局变量

class position():
    '''
    部落冲突
    职位 定位
    体系架构
    '''
    def show_msg(*args):
        # print(position_select.get())
        if position_select.get() == "首领":
            messagebox.showinfo(title='同志，欢迎加入', message='时间之外的联盟')
        elif position_select.get() == "副首":
            messagebox.showinfo(title='部落脊梁', message='雄霸一方\n专精一业\n率领部落\n走向辉煌')
        elif position_select.get() == "长老":
            messagebox.showinfo(title='中坚力量', message='联赛 竞赛 部落战\n为了部落的升级而操碎了心')
        elif position_select.get() == "成员":
            messagebox.showinfo(title='初出茅庐', message='初入新坑 请多指教')
        else:
            messagebox.showinfo(title='部落定位', message='善之以萌新\n任之以贤能\n报之以辛劳\n励志且辉煌')

    global position_select
    root = Tk()
    root.title('职务')
    name = StringVar()
    position_select = ttk.Combobox(root, textvariable=name)
    position_select["values"] = ('联盟', "首领", "副首", "长老", "成员")
    position_select["state"] = "readonly"
    position_select.current(0)
    #if __name__ == '__main__':
    #    position_select.bind("<<ComboboxSelected>>", show_msg)
    position_select.pack(fill='both', expand=1)
    Job_change = position_select.get()
    root.mainloop()
'''
if __name__ == '__main__':
    position()
'''