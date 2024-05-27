# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler
import os
import re
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_list_file = '2.ip_list.txt'
ip_list = []

commands = [
    'display current-configuration',
    'display lldp neighbor brief',
    'display ip routing-table',
    'display ospf routing',
    'display interface brief',
    'display ip interface brief',
    'display dfs-group 1 m-lag',
    'display arp',
    'display mac-address',
    'display version',
    'display esn',
    'display device manufacture-info',
    'display device',
    'display license'
]

# 读取IP列表并存储到ip_list列表中
with open(ip_list_file) as f:
    ip_list = [ip.strip() for ip in f.readlines()]

total_count = len(ip_list)  # 总IP数量
completed_count = 0  # 已执行IP数量
failed_ips = []  # 无法SSH登录的IP列表

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
datetime_str = current_datetime.strftime("%Y%m%d_%H%M%S")

def process_ip(ip):
    connection_info = {
        'device_type': 'huawei',
        'ip': ip,
        'username': 'pccw2023',
        'password': 'P@ssw0rd',
        'global_delay_factor': 1,  # 增加全局延迟因子

    }

    try:
        conn = ConnectHandler(**connection_info)
        output = ''

        for command in commands:
            output += f"Command: {command}\n"
            output += conn.send_command(command) + '\n\n'

        match = re.search(r"sysname\s+(\w+(?:-\w+)*)", output)
        if match:
            sysname = match.group(1)
            print(f"提取的sysname字段为: {sysname}")
        else:
            print("未找到sysname字段")

        # 创建文件夹并保存文件
        folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')
        os.makedirs(folder_path, exist_ok=True)  # 如果文件夹已存在，则不创建

        # 添加日期和时间到文件名
        datetime_str = current_datetime.strftime("%m%d_%Hh%Mm")
        filename = f"{sysname}_{datetime_str}.txt"
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'w') as f:
            f.write(output)
        print(f"文件已保存至：{file_path}")

    except Exception as e:
        print(f"处理 {ip} 时出错: {str(e)}")
        failed_ips.append(ip)

    finally:
        # 更新已执行IP数量
        global completed_count
        completed_count += 1
        print(f"已执行 {completed_count}/{total_count} 个IP。")

# 初始化连接池
with ThreadPoolExecutor(max_workers=5) as executor:
    # 提交每个IP的处理任务给线程池
    process_futures = [executor.submit(process_ip, ip) for ip in ip_list]

    # 等待所有任务完成
    for future in as_completed(process_futures):
        future.result()

print("所有IP执行完成。")
print(f"已完成IP列表: {completed_count}/{total_count}")
print(f"未完成IP列表: {failed_ips}")


