#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : IBM（No Chinese).py
# @Author: Persimmon
# @Date  : 2018/8/18
# @Desc  : 

import os
import speech_recognition as sr
import time
import datetime

starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'C:\Users\柿子\Desktop'):
    print("%d %s 开始转换" % (i, name))
    ##音频分块识别
    r = sr.Recognizer()
    try:
        with sr.WavFile(r'C:\Users\柿子\Desktop\%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = '090f415d-2b26-414c-aca2-6aa59ba1e6fc'
            IBM_PASSWORD = 'nHUwtSOwsX0K'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN')
            print(text)
            open(r'C:\Users\柿子\Desktop\%s.txt' % name, 'a+').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s 已完成' % (temptime,i, name))

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s 未完成' % (temptime, i, name))
        continue
endtime = datetime.datetime.now()
last=endtime-starttime
print('总共花费时间：%s'%last)
