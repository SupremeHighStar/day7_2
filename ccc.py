#!/usr/bin/env/python
# _*_ coding:utf-8 -*-

def fun():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f())
    return fs

f1=fun()
f2=fun()
f3=fun()
print (f1,f2,f3)
