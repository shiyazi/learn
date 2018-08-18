#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : find_file.py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 


import os

aim = 'readme'
path1 = '/Persimmon'
L = [x for x in os.listdir(path1) if os.path.isdir(os.path.join(path1, x))]  # 输出目录下子目录名称
print(L)

for root, dirs, files in os.walk(top=path1, topdown=True):
    for file in files:
        if aim in file:
            print(root)
            with open(os.path.join(root,'readme.txt'),'r') as f:
                print(f.read())
    continue

print(os.path.abspath('.'))
path2 = os.path.abspath('..')  # 当前目录的上一目录路径

