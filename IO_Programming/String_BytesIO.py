#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : String_BytesIO.py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 在内存中读写str和二进制数据


from io import *
f = StringIO("hello!\nI'm the world")
f.write("me")
print(f.read())

