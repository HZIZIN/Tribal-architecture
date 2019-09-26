#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 17:35:09
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

memberList = open('MemberList.txt')#, mode='rt')
dd = 1
while dd:
    dd = memberList.readline()
    print(dd.split(", "))
"""
dd = 1
while dd:
    dd = memberList.readline()
    label = [eval(x.strip()) for x in dd]
    print(label)
"""
'''
file = open('MemberList.txt', 'r')
label = [eval(x.strip()) for x in file]
print(label)
'''
