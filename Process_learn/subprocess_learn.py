#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @File  : subprocess_learn.py
# @Author: Persimmon
# @Date  : 2018/8/19
# @Desc  : 


import subprocess

print('$ nslookup www.tencent.com')
r = subprocess.call(['nslookup', 'www.tencent.com'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GB18030'))
print('Exit code:', p.returncode)