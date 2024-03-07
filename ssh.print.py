# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


from netmiko import ConnectHandler
import re


# 定义设备信息
sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

with ConnectHandler(**sw1) as connect:
        print ("已经成功登陆交换机" + sw1['ip'])
        output = connect.send_command('display interface vlan')

# 定义正则表达式模式
pattern = r'Vlanif(\d+) current state : (UP|DOWN).*?Internet Address is ([\d.]+)/\d+'

# 使用 findall 方法匹配所有符合模式的信息
matches = re.findall(pattern, output, re.DOTALL)

# 遍历匹配结果并输出信息
for match in matches:
    vlan = match[0]
    state = match[1]
    ip_address = match[2]
    print(f"VLAN {vlan} : {ip_address}")










