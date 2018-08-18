#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : find_file.py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 


import os
path1 = '/Persimmon'
L = [x for x in os.listdir(path1) if os.path.isdir(os.path.join(path1, x))]
print(L)
