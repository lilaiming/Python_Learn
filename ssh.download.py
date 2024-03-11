# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

#在192.168.56.1上运行tfp server

def ftp_file_transfer(connect, ftp_file):
    # 进入FTP模式
    connect.send_command_timing('ftp')

    # 执行FTP登录
    connect.send_command_timing('open 192.168.56.1')
    connect.send_command_timing('admin')
    connect.send_command_timing('admini')

    # 执行FTP下载（从ftp server到SW）,f'put可以上传
    connect.send_command_timing(f'get {ftp_file}')
    # 退出FTP模式
    connect.send_command_timing('quit')

with ConnectHandler(**sw1) as connect:
    print("已经成功登录交换机" + sw1['ip'])

    ftp_file = 'test123.txt'

    ftp_file_transfer(connect, ftp_file)
