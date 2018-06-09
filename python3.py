# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 17:41
# @Author  : zitan！！
# @FileName: python3.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
# age = int(input("请输入你家狗狗的年龄: "))
# print('')
# if age<0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print('你家狗狗14岁了')
# elif age == 2:
#     print('你家狗狗22岁了')
# elif age>2:
#     human=(age-2)*5
#     print('对应人类的年龄是',human)
# input('点击Enter 继续')

c,d=5,6
print(c==d)
# 该实例演示了数字猜谜游戏
guess=-1
number=10
print('猜字谜')
# while guess!=number:
#     guess=int(input("请输入你心目中的数字："))
#     if guess==number:
#         print("恭喜你答对了")
#     elif guess>number:
#         print('数字大了')
#     elif guess<number:
#         print('数字小了')
#
n=100
sum=0
con=1
while con<=n:
    sum=con+sum
    con +=1
print("1 到 %d 之和为: %d" % (n, sum))

flag=1

# while (flag):
#     print("恭喜你")
print("good luck!")
languages = ["C", "C++", "Perl", "Python"]
for b in languages:
    print (b)

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site=="Runoob":
        print("循环数据"+site)
        break
    print("循环数据"+site)
else:
    print('没有循环数据')
print('循环完成')

for i in range(0,25,5):
    print(i)
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])
var =10
while var>0:
     var=var-1
     if var==5:
      continue
     print("var 当前的值为：" ,var)
print("good luck!")
