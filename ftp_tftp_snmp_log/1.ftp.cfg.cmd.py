# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

with open('../Immd/2.ip_list.txt') as f:
    for ips in f.readlines():
        ip = ips.strip()
        connection_info = {
            'device_type': 'huawei',
            'ip': ip,
            'username': 'pccw2023',
            'password': 'P@ssw0rd',
        }

        def ftp_file_transfer(connect, ftp_file):
            try:
                # 进入FTP模式
                connect.send_command_timing('ftp')

                # 执行FTP登录
                connect.send_command_timing('open 172.17.191.88')
                connect.send_command_timing('admin')
                connect.send_command_timing('admini')

                # 执行FTP下载（从ftp server到SW）,f'put可以上传
                connect.send_command_timing(f'get {ftp_file}')
                # 退出FTP模式
                connect.send_command_timing('quit')

                print(f"成功传输文件 {ftp_file}")
            except Exception as e:
                print(f"传输文件 {ftp_file} 时出错: {str(e)}")

        with ConnectHandler(**connection_info) as connect:
            print("已经成功登录交换机" + connection_info['ip'])

            ftp_file = 'test123.txt'

            ftp_file_transfer(connect, ftp_file)



