#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : doctest_example.py
# @Author: Persimmon
# @Date  : 2018/8/15
# @Desc  : 


def fact(n):
    """
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
            ...
    ValueError: number can't below 1
    """
    if n < 1:
        raise ValueError("number can't below 1")
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()