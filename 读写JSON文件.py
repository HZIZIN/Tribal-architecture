#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 15:07:15
# @Author  : H (2066793799@qq.com)
# @Link    : https://io.org
# @Version : $Id$

import json  # 导入JSON模块
import sys  # 导入 SYS 模块


def SaveToJSON(filename, dicObject):  # 定义写JSON文件函数：SaveToJSON
    flag = False
    if type(dicObject) != dict:  # 这里只允许字典类型数据保存
        return flag
    try:  # 捕捉异常开始
        j_file = open(filename, 'w')  # 以写方式打开指定的JSON文件
        json.dump(dicObject, j_file, ensure_ascii=False)  # 以JSON格式写数据
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
    #     print('往%s写入数据出错!' % (filename))
    finally:
        if flag:
            j_file.close()  # 写完数据，关闭对应文件
    return flag  # 返回写文件是否正常标志值
# =========================================================


def GetFromJSON(filename):  # 定义读JSON文件函数 GetFromJSON
    flag = False
    dicObject = {}
    try:
        j_file = open(filename, 'r')  # 打开需要读取的JSON文件
        dicObject = json.load(j_file)  # 读取JSON文件数据，并转为Python的字典对象
        flag = True
    except:
        print("从%s读取JSON数据出错!" % (filename))
    finally:
        if flag:
            j_file.close()  # 关闭读取文件
    return dicObject  # 返回读取字典类型数据


# =========================================================


d_student = {'name': "丁丁", 'age': "12", 'birthday': "2019年6月27日"}
filename = 'student.json'  # 指定JSON文件名称
f_OK = SaveToJSON(filename, d_student)  # 调用SaveToJSON函数
if f_OK:
    print('学生信息保存到 json 文件')
else:
    sys.exit()  # 调用 SaveToJSON 函数失败，退出程序
d_get_s = GetFromJSON(filename)  # 调用 GetFromJSON 函数
if d_get_s:  # 字典值非空时，都为True,空为False
    print(d_get_s)  # 打印返回的字典对象数据
