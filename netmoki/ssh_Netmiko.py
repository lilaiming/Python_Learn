# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

# 定义设备信息
device = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

# 建立SSH连接
net_connect = ConnectHandler(**device)
output = net_connect.send_command('dis ip int b')  # 输入命令

print(output)  # 输出信息

net_connect.disconnect()  # 断开连接








