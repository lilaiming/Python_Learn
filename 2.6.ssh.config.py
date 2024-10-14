# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_list_file = '2.ip_list.txt'
ip_list = []

# 读取IP列表并存储到ip_list列表中
with open(ip_list_file) as f:
    ip_list = [ip.strip() for ip in f.readlines()]

total_count = len(ip_list)  # 总IP数量
completed_count = 0  # 已执行IP数量
failed_ips = []  # 无法SSH登录的IP列表

def process_ip(ip):
    connection_info = {
        'device_type': 'huawei',
        'ip': ip,
        'username': 'pccw2023',
        'password': 'P@ssw0rd',
        'global_delay_factor': 1,  # 增加全局延迟因子
    }

    try:
        with ConnectHandler(**connection_info) as conn:
            print(f"已经成功登录交换机 {ip}")
            # output = conn.send_config_from_file('2.cfg.cmd.txt')
            # print(output)

            # output = conn.send_command('dis cu | in loghost')
            # print(output)

            output = conn.send_command_timing(command_string="save")
            output += conn.send_command_timing(command_string="Y", strip_command=False)
            # print(output)

    except Exception as e:
        print(f"处理 {ip} 时出错: {str(e)}")
        failed_ips.append(ip)

    finally:
        global completed_count
        completed_count += 1
        print(f"已执行 {completed_count}/{total_count} 个IP。")

# 初始化连接池
with ThreadPoolExecutor() as executor:
    # 提交每个IP的处理任务给线程池
    process_futures = [executor.submit(process_ip, ip) for ip in ip_list]

    # 等待所有任务完成
    for future in as_completed(process_futures):
        future.result()

print("所有IP执行完成。")
print(f"已完成IP列表: {completed_count}/{total_count}")
print(f"未完成IP列表: {failed_ips}")

