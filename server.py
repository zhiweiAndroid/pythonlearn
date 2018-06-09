# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 9:30
# @Author  : zitan！！
# @FileName: server.py.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn
import socket
import sys

#创建socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()

port=9999

serversocket.bind(host,port)

serversocket.listen(5)

while True:
    clientsocket,addr=serversocket.accept()
    print("链接地址：%s"%str(addr))

    msg='欢迎访问菜鸟教程！'+'\r\n'

    clientsocket.send(msg.encode('utf-8'))

    clientsocket.close()

