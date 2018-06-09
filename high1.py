# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 20:28
# @Author  : zitan！！
# @FileName: high1.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配