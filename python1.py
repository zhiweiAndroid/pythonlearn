# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 10:26
# @Author  : zitan！！
# @FileName: python1.py.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("开始线程:"+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def print_time(threadName,delay,counter):

    while counter:
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1

threadLock=threading.Lock()
threads=[]


#创建线程
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)

#开启新线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)
for i in threads:
    i.join()
print("退出主线程")