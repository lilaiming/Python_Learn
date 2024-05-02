# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler
import os
import re

with open('../2.ip_list.txt') as f:
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
            output = conn.send_command('display current-configuration')
            # print(output)
            output2 = conn.save_config(cmd='save', confirm=True, confirm_response='y')
            # print(output2)
            # 使用正则表达式提取sysname后的字段
            match = re.search(r"sysname\s+(\w+(?:-\w+)*)", output)
            if match:
                sysname = match.group(1)
                print(f"提取的sysname字段为: {sysname}")
            else:
                print("未找到sysname字段")

            # 输出完整的output内容
            # print(f"完整的output内容：\n{output}")

            # 获取桌面路径
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

            # 构造文件名
            filename = f"{sysname}.txt"
            file_path = os.path.join(desktop_path, filename)

            # 将output保存为文本文件
            with open(file_path, 'w') as f:
                f.write(output)
                f.write(output2)
            # 打印保存文件的路径
            print(f"文件已保存至：{file_path}")

print("所有IP执行完成。")

