#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dir -1.py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 


import os
s = os.path.abspath('/Persimmon/test')
t = os.path.split(s)
print(t[0])

