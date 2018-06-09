# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 16:04
# @Author  : zitan！！
# @FileName: picture1.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

import urllib.request
import re
import os
url='http://bbs.voc.com.cn/topic-8391849-1-1.html'
file=urllib.request.urlopen(url)
code=file.read()
htmltext=code.decode('gbk')
pic=re.compile(r'href="(.+?\.jpg)"')
pics=pic.findall(htmltext)
path=r'test'  # r'E:\test'
if not os.path.isdir(path):
    os.makedirs(path)
x=1
for picture in pics:
    urllib.request.urlretrieve(picture, filename=r'test\%d.jpg'%x)  # filename=r'E:\test\%d.jpg'%x
    x=x+1