#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 18:05:02
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

from tkinter import *
from random_tk import *
from math import sin, cos, radians
from random import choice, uniform, randint
from time import time, sleep
from tkinter import ttk


# GRAVITY = 0.05
# colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen','indigo', 'cornflowerblue']


class initial:

    def __init__(self):
        root = Tk()
        root.title("时间之外的往事")
        # root.geometry("300x200")
        root.resizable(False, False)

        # create a popup menu
        self.menu = Menu(root, activebackground=rcolor(),
                         activeborderwidth=rnumber(), activeforeground=rcolor(),
                         bg=rcolor(), bd=rnumber(), cursor=rcursor(),
                         disabledforeground=rcolor(), font="Arial", fg=rcolor(),
                         relief="sunken", selectcolor=rcolor(), tearoff=1, title="同志 欢迎加入")
        self.menu.add_command(label="进入部落", command=self.home)

        # create a image
        self.imgbg = PhotoImage(
            file='..\\Documents\\Pictures\\Installation_package.png')
        self.label = Label(root, image=self.imgbg)
        self.label.pack()

        # attach popup to canvas
        self.label.bind("<Button-1>", self.popup)
        root.mainloop()

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def home(self):
        print("翻墙违法!")


'''
粒子的通用类

粒子几乎随机地在天空中发射，在落下并被移除之前形成一个圆形圆（星形）
从画布

属性：
      - id:星形中特定粒子的标识符
      - x, y:x，星座的y标坐（爆炸点）
      - vx, vy:x，y坐标中粒子的速度
      - total:总数：恒星中的粒子总数
      - age: 年龄：粒子在画布上的持续时间
      - color:自我解释
      - cv:canvas
      - lifespan:寿命：粒子在画布上的持续时间
      - intial_speed:爆炸时粒子的速度
'''


class part:
    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx=0., vy=0., size=2., color='red', lifespan=2, **kwargs):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        self.cv = cv
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)
        self.lifespan = lifespan

        def update(self, dt):
            # 粒子膨胀
            if self.alive() and self.expand():
                move_x = cos(radians(self.id * 360 / self.total)
                             ) * self.initial_speed
                move_y = sin(radians(self.id * 360 / self.total)
                             ) * self.initial_speed
                self.vx = move_x / (float(dt) * 1000)
                self.vy = move_y / (float(dt) * 1000)
                self.cv.move(self.cid, move_x, move_y)

            # 以自由落体坠落
            elif self.alive():
                move_x = cos(radians(self.id * 360 / self.total))
                # we technically don't need to update x, y because move will do the job
                self.cv.move(self.cid, self.vx + move_x,
                             self.vy + GRAVITY * dt)
                self.vy += GRAVITY * dt

            # 如果粒子的生命周期已过，就将其移除
            elif self.cid is not None:
                cv.delete(self.cid)
                self.cid = None

        # 定义膨胀效果的时间帧
        def expand(self):
            return self.age <= 1.2

        # 检查粒子是否仍在生命周期内
        def alive(self):
            return self.age <= self.lifespan


'''
烟花模拟循环：
递归调用以在画布上重复发出新的烟花
列表列表（星列表，每个星列都是粒子列表）
在每次通话时都在画布上创建和绘制，
通过每个“部分”对象内的更新协议
'''


def simulate(cv):
    t = time()
    explode_points = []
    wait_time = randint(10, 100)
    numb_explode = randint(6, 10)
    # 为所有模拟烟花绽放的全部粒子创建一列列表
    for point in range(numb_explode):
        objects = []
        x_cordi = randint(50, 550)
        y_cordi = randint(50, 150)
        speed = uniform(0.5, 1.5)
        size = uniform(0.5, 3)
        color = rcolor()
        explosion_speed = uniform(0.2, 1)
        total_particles = randint(10, 50)
        for i in range(1, total_particles):
            r = part(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
                     vx=speed, vy=speed, color=color, size=size, lifespan=uniform(0.6, 1.75))
            objects.append(r)
        explode_points.append(objects)

    total_time = .0
    # 在1.8秒时间帧内保持更新
    while total_time < 1.8:
        sleep(0.01)
        tnew = time()
        t, dt = tnew, tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    # recursive call to continue adding new explosion on canvas
    root.after(wait_time, simulate, cv)


def close(*ignore):
    """Stops simulation loop and closes the window."""
    global root
    root.quit()


if __name__ == '__main__':
    initial()
    '''
    root = Tk()
    cv = Canvas(root, height=600, width=600)
    # 绘制一个
    photo = PhotoImage(
        file='..\\..\\Documents\\Pictures\\Installation_package.png')
    cv.create_image(0, 0, image=photo, anchor='nw')
    cv.pack()
    root.protocol("WM_DELETE_WINDOW", close)
    # 在1秒后才开始调用stimulate()
    root.after(100, simulate, cv)
    root.mainloop()
    '''
