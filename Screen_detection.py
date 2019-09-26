#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-01 18:16:13
# @Author  : IOqbit (ioqbit@163.com)
# @Link    : https://hzizin.github.io/
# @Version : $Id$

import tkinter as tk
from random_tk import *  # 随机模块儿
import tkinter.colorchooser as cc  # 用户自定义颜色
from tkinter import messagebox  # 弹窗提示是否确认


def shutdown():
    root.destroy()


def donothing():
    pass


def callback(event):
    '''显示当前鼠标坐标'''
    pri.set("X:%d\nY:%d" % (event.x, event.y))


def change_color():
    '''用户自定义背景颜色'''
    (rgb, hx) = cc.askcolor()
    if messagebox.askyesno("是否将其设为背景色", 'RGB: ' + str(rgb) + "\nHEX: " + hx):
        frame.config(bg=hx)


def choose_color():
    '''选取颜色值模块儿'''
    global rgb, hx
    (rgb, hx) = cc.askcolor()
    return rgb, hx


def colorchange():
    '''可修改颜色控件集合 用户自定义'''
    def bucong_choosecolorchange():
        '''指令补充 lambda'''
        choose_color()
        coc_label.config(fg=hx, font="Arial -20", height=2)
        coc_label.config(text='RGB: ' + str(rgb) + "\nHex: " + hx)
        coc.config(height=300, width=200)

    global rgb, hx
    # rgb, hx = choose_color()
    coc = tk.Toplevel(bg='blue', bd=3, cursor="circle", relief='ridge')
    coc.title("可修改颜色控件集合")
    coc.attributes('-topmost', 1)
    coc.geometry('{}x{}+{}+{}'.format(450, 130, int(screenwidth / 2),
                                      int(screenheight / 2)))
    coc.resizable(1, 1)
    coc.minsize(445, 50)
    # coc.maxsize(1024, 796)
    coc_label = tk.Label(coc, text="选取颜色 进行个性化设置", relief="groove", bd=10,
                         font="Arial -30", fg=hx, bg=rcolor(), height=1, width=20, padx=35, pady=10,)
    coc_label.pack(side='top', fill="both", expand=1)
    panel = tk.Frame(coc)
    button1 = tk.Button(panel, text="主体背景色", bd=3, relief='groove',
                        command=lambda: frame.config(bg=hx))
    button2 = tk.Button(panel, text="文本显示台", bd=3, relief='groove',
                        command=lambda: prin.config(bg=hx))
    button3 = tk.Button(panel, text="文本颜色", bd=3, relief='groove',
                        command=lambda: prin.config(fg=hx))
    button4 = tk.Button(panel, text="选取颜色", bd=3, relief='groove', bg=rcolor(),
                        command=bucong_choosecolorchange)
    button1.pack(side='left', fill='both', expand=1)
    button2.pack(side='left', fill='both', expand=1)
    button3.pack(side='left', fill='both', expand=1)
    button4.pack(side='right', fill='both', expand=1)
    panel.pack(side='bottom', fill='both', expand=1)


def change_size():
    size_scale = tk.Toplevel(bg='blue', bd=3, cursor="circle", relief='ridge')
    scale = tk.Scale(size_scale, from_=10, to=100, command=donothing)
    scale.set(12)
    scale.pack(side="right", fill="both", expand=1)
    s = tk.Scale(size_scale, label='戏子戏精指数', from_=0, to=12, orient=tk.HORIZONTAL,
                 length=200, showvalue=0, tickinterval=2, resolution=0.01, command=donothing)
    s.pack(fill='x', side='bottom')


def instructions():
    '''使用说明'''
    messagebox.showinfo('user',
                        "未移动鼠标时显示背景色面积\n\n移动鼠标显示窗口内光标位置\n按住并移动鼠标显示全屏坐标\n\n双击左键 中键 右键\n最小化 关闭 最大化\n")


root = tk.Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.title('屏幕检测')
root.geometry('{}x{}+{}+{}'.format(int(screenwidth / 1.2),
                                   int(screenheight / 1.5), 0, 0))
root.iconbitmap('..\\Documents\\Pictures\\Mozilla.ico')
root.attributes('-topmost', 0)  # 正常窗口，允许其它窗口覆盖
root.attributes("-toolwindow", 0)  # 设置工具栏样式窗口为普通
root.overrideredirect(False)  # 恢复显示窗口标题栏
root.state("zoomed")  # 设置为普通窗口(最大化 最小化)
root.attributes("-fullscreen", False)  # 取消全屏窗口，还原为普通窗口。
root.attributes("-alpha", 1)

rootbg = rgb = hx = rcolor()
frame = tk.Frame(root, background=rootbg, bd=50)
pri = tk.StringVar()
pri.set(rootbg + "\n宽:" +
        str(screenwidth) + "\n高" + str(screenheight))

menubar = tk.Menu(root, bg=rcolor(), fg=rcolor(), bd=20, cursor=rcursor(),
                  selectcolor=rcolor(), tearoff=1, title="屏幕大小 分辨率检测")
setupmenu = tk.Menu(menubar, tearoff=0)
setupmenu.add_command(label="窗体背景颜色", command=change_color)
setupmenu.add_command(label="可修改颜色集", command=colorchange)
setupmenu.add_command(label="透明度", command=change_size)
setupmenu.add_separator()
setupmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="设置", menu=setupmenu)

aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label="关于作者", command=colorchange)
aboutmenu.add_command(label="使用说明", command=instructions)
menubar.add_cascade(label="About", menu=aboutmenu)

prin = tk.Label(frame, textvariable=pri, height=3, width=20, padx=35, pady=10,
                background=rcolor(), relief="ridge", borderwidth=1, foreground="red")
prin.pack(side='top')

root.bind("<Motion>", callback)
# frame.bind("<B1-Motion>", callback)
frame.bind("<B2-Motion>", callback)
frame.bind("<B3-Motion>", callback)
# frame.bind("<ButtonRelease-3>", Coloring)
frame.bind("<Double-Button-3>", shutdown)
frame.bind("<Double-Button-2>", shutdown)
frame.pack(side='top', fill='both', expand=1)

root.config(menu=menubar)
root.mainloop()
