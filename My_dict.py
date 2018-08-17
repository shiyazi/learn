#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : My_dict.py
# @Author: Persimmon
# @Date  : 2018/8/17
# @Desc  : 


class Dict(dict):
    """
        Simple dict but also support access as x.y style.

        >>> d1 = Dict()
        >>> d1['x'] = 100
        >>> d1.x
        100
        >>> d1.y = 200
        >>> d1['y']
        200
        >>> d2 = Dict(a=1, b=2, c='3')
        >>> d2.c
        '3'
        >>> d2['empty']
        Traceback (most recent call last):
            ...
        KeyError: 'empty'
        >>> d2.empty
        Traceback (most recent call last):
            ...
        AttributeError: 'Dict' object has no attribute 'empty'
        """

    def __init__(self, **kw):
        super().__init__(**kw)  # super方法从父类调用方法，即将传入参数按照父类的参入参数的处理方式处理

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
