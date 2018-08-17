#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : property.py
# @Author: shi zi
# @Date  : 2018/8/15
# @Desc  :


class Screen(object):
    def __init__(self):
        pass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be int')
        if value < 0 or value > 10000:
            raise ValueError('value must between 0`10000')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be int')
        if value < 0 or value > 10000:
            raise ValueError('height must between 0`10000')
        self.__height = value

    @property
    def resolution(self):
        return 786432


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

print(s.height)