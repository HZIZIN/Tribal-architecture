#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 14:10:58
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import tkinter as tk
from tkinter import ttk
from random_tk import *


def popup(event):
    '''右键菜单显示'''
    menu.post(event.x_root, event.y_root)


def treeview_sort_column(tv, col, reverse):
    '''Treeview、列名、排列方式'''
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式 reverse=True or Flase
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
    # 重写标题，使之成为再点倒序的标题

# ===========================================================================内容选取
# ttk treeview的样式设定 奇数行背景浅蓝色。有一个问题，就是选中了奇数行后，其背景色不变！暂时未破解。


def brush_treeview(self, tv):
    """
    改变treeview样式
    :param tv:
    :return:
    """
    if not isinstance(tv, ttk.Treeview):
        raise Exception("argument tv of method bursh_treeview must be instance of ttk.TreeView")
    # =============给bom_lines设置样式=====
    items = tv.get_children()
    for i in range(len(items)):
        if i % 2 == 1:
            tv.item(items[i], tags=('oddrow'))
    tv.tag_configure('oddrow', background='#eeeeff')
# =================================================================未解决


def LeftMouseClickToRelease(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('点击选中了:', item_text[:])  # 输出所选行的'第一列的'值


def treeviewClick(event):  # 双击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print('双击:', item_text[0])  # 输出所选行的第一列的值
    # 双击修改内容 未完
    from Organization import position
    position()
    a = position.Job_change
    print(a)
    # item_text[0] = a 元组


# def tipscopy(event):
def tipscopy():
    '''成员信息查看'''
    content = tk.StringVar()
    tiptle = 'TitleName'
    for item in tree.selection():
        item_text = tree.item(item, "values")
        content.set(item_text[:])
        tiptle = '时间之外的往事 ' + item_text[-1]  # 受‘离线成员’开发中功能影响 故删减
        # tiptle = '时间之外的往事 ' + item_text[2]  + ' ' + item_text[-1]
    tipwindows = tk.Toplevel()
    #tipwindows.geometry('550x45')  # 大小和列表长度相关
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    tipwindows.geometry('{}x{}+{}+{}'.format(550, 53,
        int(root_width / 2), int(root_height / 2)))
    tipwindows.resizable(True, False)
    tipwindows.title(tiptle)
    e1 = tk.Entry(tipwindows, textvariable=content, state="readonly",
        bg=rcolor(), bd=3, cursor=rcursor(), exportselection=1, fg=rcolor(),
        selectbackground=rcolor(), selectborderwidth=4, selectforeground=rcolor())
    e1.pack(padx=10, pady=10, fill='both', expand=1)  # 外边框 可拉伸


def delAll(treeName):
    '''删除所有元素 清空内容'''
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    # ====================另一种方法
    # items = your_treeview.get_children()
    # [your_treeview.delete(item) for item in items]


def delSelectedContent(treeName):
    '''删除选定行内容'''
    # x=tree.get_children()
    # for item in x:
    for item in tree.get_children():
        item_text = tree.item(item, "values")
        try:  # 捕捉异常开始
            print('本应删除', item_text)
            tree.delete(item_text)
        except ValueError:
            print('对象值不正确')
        except IndexError:
            print('在指定的字符串、元组、列表等序列对象的下标元素不存在')
        except NameError:
            print('指定的对象名不存在')
        except KeyError:
            print('指定的字典键不存在')
        except TypeError:
            print('指定了错误类型的对象')
        except ModuleNotFoundError:
            print('模块文件找不到或模块文件名写错')
        except SyntaxError:
            print('语法无效')
        except AttributeError:
            print('对象属性、方法引用或赋值不当')
        finally:
            print('\n删除语句出错\n')


# `````````````````````````````````````Main````````````````````````````````````
# 设置show属性为 headings 即可隐藏首列。
# height 行
root = tk.Tk()
root.title("组织名单")
columns = ["zero", "one", "two", "three", "four", "five", "six","seven","eight","nine","ten"]
headtext = ["排名", "落 网 时 间", "职务", "竞赛", "联赛","DAY", "星", "捐兵", "收兵", "额外奖励", "组织内部代号"]
tree = ttk.Treeview(root, columns=columns, height=18, style="mystyle.Treeview")#, show="headings")  # 调用外部样式
# 多少列，宽度和最小宽度。通过定义stretch=tk.NO，用户无法修改列的宽度。
tree.column("zero", width=31, minwidth=30, stretch=tk.NO)
tree.column("one", width=90, minwidth=90, stretch=tk.NO)
tree.column("two", width=35, anchor='center')
tree.column("three", width=55)
tree.column("four", width=55)
tree.column("five", width=90)
tree.column("six", width=10)
tree.column("seven", width=43)
tree.column("eight", width=44)
tree.column("nine", width=66)
tree.column("ten", width=105)
#  =================================================================文本读取段
memberList = open('FiveThousand.txt', mode='rt', encoding='ansi')
dd = 1
xulie = 0
buding_xulie = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
while dd:
    dd = memberList.readline()

    if dd == '':  # 去除末尾空行
        break

    if dd == ".\n":
        print("已触发 离线成员加入")
        id1 = tree.insert("", xulie, "dir2", text="远方")
        xulie += 1
        offlinename = dd.split(", ")
        tree.insert(id1, "end", xulie, text="元老", values=offlinename)
        continue
        # break

    cyname = dd.split(", ")  # 生成列表 检测英文逗号分隔列表元素

    if cyname[0] == '#':  # 跳过注释行
        continue

    # xulie += 1  # 判断块'前 后',从'一'开始产生名次顺序(else依赖 注意修改列表或插入语句)
    if xulie >= 10:  # Sort()排序按照ASCII码，比较位数上的大小，此番修改了与需求所需的偏差
        cyname.insert(1, xulie)  # 在列表1处添加序列号，插入处依赖
    elif xulie < 10:  # 10以后的‘排名’数字正常 符合需求
        cyname.insert(1, buding_xulie[xulie])
    xulie += 1  # 判断块'前 后',从'零'开始产生名次顺序(else依赖 注意修改列表或插入语句)
    tree.insert("", xulie, text=cyname[0], values=cyname[1:])

scroll_y = tk.Scrollbar(root, orient="vertical", command=tree.yview)
scroll_y.pack(side="right", expand=False, fill="y")
tree.configure(yscrollcommand=scroll_y.set)  # 这三行创建并绑定滚动条
tree.pack(fill='both', expand=1)
# ============================================================================右键菜单
menu = tk.Menu(root, tearoff=1, title='组织架构调整', cursor=rcursor())
menu.add_command(label="查看 信息", command=tipscopy)
menu.add_command(label="编辑 信息", command=tipscopy)
menu.add_separator()
menu.add_command(label="移至'离线'", command=tipscopy)
# ==========================================================================点击标题排序
i = 0  # 索引修改标题
for col in columns:  # 给所有标题加（循环上边的“手工”）
    tree.heading(col, text=headtext[i],
        command=lambda _col=col: treeview_sort_column(tree, _col, False))
    i += 1
# ==============================================
tree.bind('<ButtonRelease-3>', popup)  # 绑定右键双击离开事件===========
# tree.bind('<ButtonRelease-1>', LeftMouseClickToRelease)  # 绑定左键单击离开事件
# tree.bind('<Double-1>', lambda dleName: delAll(tree))
# tree.bind('<Double-3>', lambda dleName: delSelectedContent(tree))


root.mainloop()
"""
各种点击事件

鼠标左键单击按下    1/Button-1/ButtonPress-1     
鼠标左键单击松开    ButtonRelease-1  
鼠标右键单击  3    
鼠标左键双击  Double-1/Double-Button-1     
鼠标右键双击  Double-3     
鼠标滚轮单击  2    
鼠标滚轮双击  Double-2     
鼠标移动    B1-Motion    
鼠标移动到区域 Enter    
鼠标离开区域  Leave    
获得键盘焦点  FocusIn  
失去键盘焦点  FocusOut     
键盘事件    Key  
回车键 Return   
控件尺寸变   Configure
"""
