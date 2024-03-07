# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

# 定义设备信息
sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

commands = ['interface LoopBack1', 'description test-python-1234']
with ConnectHandler(**sw1) as connect:
        print ("已经成功登陆交换机" + sw1['ip'])
        output = connect.send_command('dis interface description | include Loop')
        print(output)
        output = connect.send_config_set(commands)
        print(output)
        output = connect.send_config_from_file('loopback.txt')
        print(output)
        output = connect.send_command('dis interface description | include Loop')
        print(output)
        output = connect.save_config(cmd='save', confirm=True, confirm_response='y')
        print(output)










