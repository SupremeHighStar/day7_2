#!/usr/bin/env/python
# _*_ coding:utf-8 -*-

import string
import random

passwd = string.ascii_letters + "0123456789"
s = ""

for i in range(8):
    s += random.choice(passwd)

print (s)