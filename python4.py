# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 19:35
# @Author  : zitan！！
# @FileName: python4.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
# def hello():
#     print("hello world!")
# hello()
# a = 10
# def test(a=5):
#     a = a + 1
#     print(a)
# test()

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

a=[vec1[i]*vec2[i] for i in range(len(vec1))]
print(len(vec1))
for i in range(len(vec1)):
    print(i)
print(a)
b=[str(round(355/133,i)) for i in range (1,6)]
print(b)
c=dict(name="lilei",age=28,gender="女")
print(c)
for k,v in c.items():
    print(k,v)


for i ,v in enumerate(vec1):
    print(i,v)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)
s='hello world'
str(s)
for x in range(1, 11):
      print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))