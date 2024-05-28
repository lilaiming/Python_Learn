# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os
import logging
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_list_file = '2.ip_list.txt'
commands_file = '2.cfg.cmd.txt'
ip_list = []
commands_paragraphs = []

# 读取IP列表并存储到ip_list列表中
with open(ip_list_file) as f:
    ip_list = [ip.strip() for ip in f.readlines()]

# 读取要检查的命令段落列表并存储到 commands_paragraphs 列表中
with open(commands_file) as f:
    commands_paragraphs = [paragraph.strip() for paragraph in f.read().split('\n\n')]

total_count = len(ip_list)  # 总IP数量
completed_count = 0  # 已执行IP数量
failed_ips = []  # 无法SSH登录的IP列表

# 获取桌面文件夹路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 配置日志记录
log_folder = os.path.join(desktop_path, 'output_folder')
log_file = 'network_audit.log'
log_path = os.path.join(log_folder, log_file)
logging.basicConfig(filename=log_path, level=logging.INFO)

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
        output = conn.send_command('display current-configuration')

        for paragraph in commands_paragraphs:
            count = output.count(paragraph)
            if count > 0:
                message = f"设备 {ip} 中命令段落存在了 {count} 次:\n{paragraph}"
                print(message)
                logging.info(message)
            else:
                message = f"设备 {ip} 中命令段落不存在:\n{paragraph}"
                print(message)
                logging.info(message)
                failed_ips.append(ip)

    except Exception as e:
        message = f"处理 {ip} 时出错: {str(e)}"
        print(message)
        logging.error(message)
        failed_ips.append(ip)

    finally:
        # 更新已执行IP数量
        global completed_count
        completed_count += 1
        message = f"已执行 {completed_count}/{total_count} 个IP。"
        print(message)
        logging.info(message)


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

print("不存在命令的IP列表:")
for ip in failed_ips:
    print(ip)


