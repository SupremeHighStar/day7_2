#!/usr/bin/env/python
# _*_ coding:utf-8 -*-



aaa = ("""
            [1] aaa
            [2] bbb
            [q] quit
            suru:
    """)
sr = raw_input(aaa)

while not (sr == "1" or sr == "2" ):
     sr = sr = raw_input(aaa)

     if sr == "q":
         break

