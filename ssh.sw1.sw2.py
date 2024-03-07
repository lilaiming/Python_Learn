# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 第一种情况：生产网络里所有设备的username, password, port这些参数都一样
from netmiko import ConnectHandler

with open('ip_list.txt') as f:
    for ips in f.readlines():
        ip = ips.strip()
        connection_info = {
                'device_type': 'huawei',
                'ip': ip,
                'username': 'pccw2023',
                'password': 'P@ssw0rd',
        }
        with ConnectHandler(**connection_info) as conn:
            print (f'已经成功登陆交换机{ip}')
            output = conn.send_command('dis cu | in sysname')
            print(output)


#第二种情况：生产网络里设备的username, password, port这些参数不尽相同
# import json
# from netmiko import ConnectHandler
#
# with open("switches.json") as f:
#     devices = json.load(f)
# for device in devices:
#     with ConnectHandler(**device['connection']) as conn:
#         hostname = device['name']
#         print (f'已经成功登陆交换机{hostname}')
#         output = conn.send_command('dis cu | in sysname')
#         print(output)





