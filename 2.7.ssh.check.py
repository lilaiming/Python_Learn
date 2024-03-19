# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com
#
# from netmiko import ConnectHandler
# import re
# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# ip_list_file = '2.ip_list.txt'
# commands_file = '2.cfg.cmd.txt'
# ip_list = []
# commands = []
#
# # 读取IP列表并存储到ip_list列表中
# with open(ip_list_file) as f:
#     ip_list = [ip.strip() for ip in f.readlines()]
#
# # 读取要检查的命令列表并存储到commands列表中
# with open(commands_file) as f:
#     commands = [cmd.strip() for cmd in f.readlines()]
#
# total_count = len(ip_list)  # 总IP数量
# completed_count = 0  # 已执行IP数量
# failed_ips = []  # 无法SSH登录的IP列表
#
#
# def process_ip(ip):
#     connection_info = {
#         'device_type': 'huawei',
#         'ip': ip,
#         'username': 'pccw2023',
#         'password': 'P@ssw0rd',
#         'global_delay_factor': 1  # 设置全局延迟因子，默认值是0.1
#     }
#
#     try:
#         conn = ConnectHandler(**connection_info)
#         output = conn.send_command('display current-configuration')
#
#         for cmd in commands:
#             match = re.search(re.escape(cmd), output)
#             if match:
#                 print(f"设备 {ip} 中存在命令 '{cmd}'")
#             else:
#                 print(f"设备 {ip} 中不存在命令 '{cmd}'")
#                 failed_ips.append(ip)
#
#     except Exception as e:
#         print(f"处理 {ip} 时出错: {str(e)}")
#         failed_ips.append(ip)
#
#     finally:
#         # 更新已执行IP数量
#         global completed_count
#         completed_count += 1
#         print(f"已执行 {completed_count}/{total_count} 个IP。")
#
#
# # 初始化连接池
# with ThreadPoolExecutor(max_workers=5) as executor:
#     # 提交每个IP的处理任务给线程池
#     process_futures = [executor.submit(process_ip, ip) for ip in ip_list]
#
#     # 等待所有任务完成
#     for future in as_completed(process_futures):
#         future.result()
#
# print("所有IP执行完成。")
# print(f"已完成IP列表: {completed_count}/{total_count}")
# print(f"未完成IP列表: {failed_ips}")
#
# print("不存在命令的IP列表:")
# for ip in failed_ips:
#     print(ip)


from netmiko import ConnectHandler
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_list_file = '2.ip_list.txt'
commands_file = '2.cfg.cmd.txt'
ip_list = []
commands = []

# 读取IP列表并存储到ip_list列表中
with open(ip_list_file) as f:
    ip_list = [ip.strip() for ip in f.readlines()]

# 读取要检查的命令列表并存储到commands列表中
with open(commands_file) as f:
    commands = [cmd.strip() for cmd in f.readlines()]

total_count = len(ip_list)  # 总IP数量
completed_count = 0  # 已执行IP数量
failed_ips = []  # 无法SSH登录的IP列表


def process_ip(ip):
    connection_info = {
        'device_type': 'huawei',
        'ip': ip,
        'username': 'pccw2023',
        'password': 'P@ssw0rd',
        'global_delay_factor': 1  # 设置全局延迟因子，默认值是0.1
    }

    try:
        conn = ConnectHandler(**connection_info)
        output = conn.send_command('display current-configuration')

        for cmd in commands:
            count = output.count(cmd)
            if count > 0:
                print(f"设备 {ip} 中命令 '{cmd}' 出现了 {count} 次")
            else:
                print(f"设备 {ip} 中命令 '{cmd}' 未出现")
                failed_ips.append(ip)

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

print("不存在命令的IP列表:")
for ip in failed_ips:
    print(ip)


