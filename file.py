# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 21:17
# @Author  : zitan！！
# @FileName: file.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
f = open("/foo.txt", "w")
num=f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print("num :",num)
f.close()
f=open("/foo.txt", "r")
s=f.readlines()
print(s)
for line in f:
    print(line,end=' ')

# 打开一个文件
f = open("/foo1.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

# 关闭打开的文件
f.close()
f=open("/foo1.txt", "r")
s=f.readlines()
print(s)

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
import pickle,pprint
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()