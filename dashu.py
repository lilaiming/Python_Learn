# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# print('-'*80)
#
# print ('请输入您的姓名')
# name1 = input()
# print('my mane is ' + name1)

# IP = '192.168.1.1'
# protocol = 'https'
# url = 'api/v1/network/status'
#
# URL = '{}:{}{}'.format(protocol,IP,url)
#
# print(URL)
#


def URL1(ip, protocol, url):
    x = '{}:{}{}'.format(protocol, ip, url)
    return x

y = URL1('10.1.1.1','https','qytang666')
print(y)

















