#!/usr/bin/env/python
# _*_ coding:utf-8 -*-

import os
import sys

def fun1(path):
    dirs = os.path.exists(path)
    if dirs:
        print("文件夹依存在")
        pass
    else:
        os.makedirs(path)
        print("文件夹创建成功")

def fun2(files):
    b = open(files,"w")
    b.close()



fun1(sys.argv[1])

