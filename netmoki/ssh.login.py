# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

# 定义设备信息
sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.13.119',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

with ConnectHandler(**sw1) as connect:
	print ("已经成功登陆交换机" + sw1['ip'])
