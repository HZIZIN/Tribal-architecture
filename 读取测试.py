#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 14:45:15
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import json
import sys  # 导入 SYS 模块



def GetFromJSON(filename):  # 定义读JSON文件函数 GetFromJSON
    flag = False
    arrayObject = []
    try:
        j_file = open(filename, 'r')  # 打开需要读取的JSON文件
        arrayObject = json.load(j_file)  # 读取JSON文件数据
        flag = True
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
    # except:
    # print("从%s读取JSON数据出错!" % (filename))
    finally:
        if flag:
            j_file.close()  # 关闭读取文件
    return arrayObject  # 返回读取类型数据


filename = 'student.json'#'MemberList.JSON'  # 指定JSON文件名称
d_get_s = GetFromJSON(filename)  # 调用 GetFromJSON 函数
if d_get_s:  # 值非空时，都为True,空为False
    print(d_get_s)  # 打印返回的对象数据

'''
memberList = open('MemberList.txt')#, mode='rt')
dd = 1
while dd:
    dd = memberList.readline()
    print(dd)

memberList = 'MemberList.JSON'
mylist = GetFromJSON(memberList)
print(mylist)

#jsontxt = open('MemberList.json', mode='a')
for i in range(51):
    namelist = memberList.readline()
    print(namelist)
    #jsontxt.write(namelist)
a = ['51', "Test", "Test", "Test", "Test", "Test", "Test"]
print(a)
'''
