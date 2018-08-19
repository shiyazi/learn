#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : multiprocessing_learn.py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 

from multiprocessing import *
import os


def run_proc(name):
    print('Run the process %s %s' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')