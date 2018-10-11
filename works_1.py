#!/usr/bin/env/python
# _*_ coding:utf-8 -*-

def fun(Spath,Dpath):
    Sfile = open(Spath,"r")
    Dfile = open(Dpath,"a")
    for i in Sfile:
        Dfile.write(i)
        Dfile.flush()
    else:
        Dfile.close()

a = raw_input("请输入复制文件（包括文件路径）:")
b = raw_input("复制到哪里(路径):")

fun(a,b)