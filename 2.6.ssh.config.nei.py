# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import re
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

            # 获取Model
            output_Model = conn.send_command('display version')
            pattern = r"Version \d+\.\d+ \((.*) V\d+R\d+C\d+SPC\d+\)"
            matches = re.search(pattern, output_Model)
            Model = matches.group(1)
            # print(Model)

            output = conn.send_command('display lldp neighbor brief')
            # print(output)

            if Model in ["CE16800", "CE8850EI", "CE6863E", "CE6881"]:
                # 解析输出并进行配置 //CE系列交换机
                lines = output.splitlines()[2:]  # 去除前两行标题
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 4:  # 确保存在足够的数据
                        local_interface = parts[0]
                        neighbor_interface = parts[2]
                        neighbor_device = parts[3]

                        # 构建配置命令
                        interface = local_interface.split()[0]
                        description = f"To_{neighbor_device}_{neighbor_interface}"
                        config_commands = [f"interface {interface}", f"description {description}"]
                        # print(config_commands)

                        # 发送配置命令
                        output = conn.send_config_set(config_commands, exit_config_mode=False)
                        # print(output)

            else:
                # 解析输出并进行配置 //S系列交换机
                lines = output.splitlines()[1:]  # 去除前两行标题
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 4:  # 确保存在足够的数据
                        local_interface = parts[0]
                        if "100GE" not in local_interface:
                            local_interface = local_interface.replace("GE" , "GigabitEthernet").replace("XGE", "XGigabitEthernet")
                        neighbor_device = parts[1]
                        neighbor_interface = parts[2]

                        # 构建配置命令
                        interface = local_interface.split()[0]
                        description = f"To_{neighbor_device}_{neighbor_interface}"
                        config_commands = [f"interface {interface}", f"description {description}"]
                        # print(config_commands)

                        # 发送配置命令
                        output = conn.send_config_set(config_commands , exit_config_mode=False)
                        # print(output)

            output = conn.send_command_timing(command_string="commit")
            output = conn.send_command_timing(command_string="return")
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
with ThreadPoolExecutor(max_workers=5) as executor:
    # 提交每个IP的处理任务给线程池
    process_futures = [executor.submit(process_ip, ip) for ip in ip_list]

    # 等待所有任务完成
    for future in as_completed(process_futures):
        future.result()

print("所有IP执行完成。")
print(f"已完成IP列表: {completed_count}/{total_count}")
print(f"未完成IP列表: {failed_ips}")

