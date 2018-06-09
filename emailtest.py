# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 9:43
# @Author  : zitan！！
# @FileName: emailtest.py.py
# @Software: PyCharm
# @Blog    ：http://zhizhiwei.cn

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '2822252841@qq.com'  # 发件人邮箱账号
my_pass = '037164021951'  # 发件人邮箱密码
my_user = '2822252841@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('今天天气不错', 'plain', 'utf-8')
        msg['From'] = formataddr(["From1213082309", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")