# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 10:15
# @Author  : zitan！！
# @FileName: thread.py.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

import _thread
import threading
import time
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s"%(threadName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
except:
    print("error:not run")

while 1:
    pass

exitFlag=0





