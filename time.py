# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 11:54
# @Author  : zitan！！
# @FileName: time.py.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
import time

#如函数time.time()用于获取当前时间戳
t=time.time()
print("当前的时间戳: %s"%t)

localtime=time.localtime(time.time())
print("本地时间为 :",localtime)

localtime=time.asctime(localtime)
print("本地时间为",localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.localtime())
s=time.strftime("%Y-%m-%d  %H-%M-%S",time.localtime())
print(s)

print(time.mktime(time.strptime(s,"%Y-%m-%d  %H-%M-%S")))

import calendar
cal=calendar.month(2018,6)
print("当月日历为：")
print(cal)

