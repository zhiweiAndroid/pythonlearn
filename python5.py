# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 11:38
# @Author  : zitan！！
# @FileName: python5.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

datas=json.loads(json_str)
print('datas[name]',datas['name'])
print('datas[url]',datas['url'])

with open('data.json','w') as f:
    json.dump(data,f)

with open('data.json','r') as  f:
    s=json.load(f)
    print(s)