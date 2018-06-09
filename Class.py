# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 19:15
# @Author  : zitan！！
# @FileName: Class.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说 ：我 %d 岁。"%(self.name,self.age))


p = people('李萌萌',22,90)
p.speak()

class student(people):
    grade=0
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s 说 ：我 %d 岁,我上 %d 年级" % (self.name, self.age,self.grade))
s=student('张梓琳',12,98,8)
s.speak()

class hero:
    __name=''
    age=0
    def __init__(self,n,a):
        self.__name=n
        self.age=a
    def show(self):
        print('%s is a hero,today he is %d years old'%(self.__name,self.age))

h=hero('孙悟空',140000)
h.show()

import math
print(math.pi)

from urllib.request import urlopen
from urllib.request import Request
import urllib
from urllib.parse import urlencode
from  datetime import date
now=date.today()
print(now)
birthday=date(1991,1,31)
age=now-birthday
print(age.days)

#请求网络
url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
req_data=urlencode(date)
res=urlopen(url+'?'+req_data)
res=res.read().decode()
print(res)

data=data.encode('ascii')
req_data=Request(url,data)
with urlopen(req_data) as res:
    res=res.read().decode()

print(res)

