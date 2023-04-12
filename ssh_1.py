# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


# import paramiko
# import time
#
# ip = "10.109.64.136"; user = 'lenovo'; password = 'Lenovo,!'
#
# ssh1 = paramiko.SSHClient()
# ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh1.connect(hostname=ip,port=22,username=user,password=password,timeout=5,
#              allow_agent=False,look_for_keys=False)
# cli = ssh1.invoke_shell()
# cli.send('enable\n')
# time.sleep(2)
# cli.send('Lenovo,!\n')
# time.sleep(2)
# cli.send('terminal len 0\n')
# time.sleep(2)
# cli.send('show run\n')
# time.sleep(2)
# running = cli.recv(99999).decode()
# print(running)
#
# time.sleep(15)
# ssh1.close()

import paramiko
import time

device_list = [
{"device_name":'SW1','ip':'203.0.113.1','username':'qytang','password':'qytang','plat':'IOS'},
{"device_name":'SW2','ip':'203.0.113.2','username':'qytang','password':'qytang','plat':'IOS'},
{"device_name":'SW3','ip':'203.0.113.3','username':'qytang','password':'qytang','plat':'HW'},
{"device_name":'SW4','ip':'203.0.113.4','username':'qytang','password':'qytang','plat':'HW'}
]

def cisco(ip,username,password):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认密钥处理策略
    ssh1.connect(hostname=ip, port=22, username=username, password=password,
                 timeout=5, allow_agent=False, look_for_keys=False)
    cli = ssh1.invoke_shell()
    cli.send('enable\n')
    time.sleep(1)
    reply = cli.recv(99999).decode()
    # print(reply)
    cli.send('qytang\n')
    time.sleep(1)
    reply = cli.recv(99999).decode()
    # print(reply)
    cli.send('terminal len 0\n')
    time.sleep(1)
    reply = cli.recv(99999).decode()
    # print(reply)
    cli.send('show run\n')
    time.sleep(1)
    running = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return running

def huawei(ip,username,password):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认密钥处理策略
    ssh1.connect(hostname=ip, port=22, username=username, password=password,
                 timeout=5, allow_agent=False, look_for_keys=False)
    cli = ssh1.invoke_shell()
    cli.send('screen-length 0 temporary\n')
    time.sleep(1)
    reply = cli.recv(99999).decode()
    # print(reply)
    cli.send('dis cur\n')
    time.sleep(1)
    running = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return running

for i in range(len(device_list)):
    device_name =device_list[i]['device_name']
    ip = device_list[i]['ip']
    username = device_list[i]['username']
    password = device_list[i]['password']
    plat = device_list[i]['plat']
    if plat == 'IOS':
        running = cisco(ip,username,password)
    elif plat == 'HW':
        running = huawei(ip, username, password)
    else:
        print('error')
    print(running)







