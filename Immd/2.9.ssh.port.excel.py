# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email: essid@qq.com

import os
import re
import datetime
import pandas as pd
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
results = []  # 存储结果


def process_ip(ip):
    connection_info = {
        'device_type': 'huawei',
        'ip': ip,
        'username': 'pccw2023',
        'password': 'P@ssw0rd',
        'global_delay_factor': 2,  # 增加全局延迟因子
    }

    try:
        with ConnectHandler(**connection_info) as conn:
            print(f"已经成功登录交换机 {ip}")

            # 获取Sysname
            output_sysname = conn.send_command('display current-configuration | include sysname')
            pattern = r"sysname (.*)"
            matches = re.search(pattern, output_sysname)
            Sysname = matches.group(1) if matches else "未知"

            # 获取接口配置
            output_interface = conn.send_command('display current-configuration interface')

            # 解析接口配置
            interface_results = parse_interface_config(output_interface)

            # 存储结果
            for result in interface_results:
                results.append({'Hostname': Sysname, 'IP': ip, **result})

    except Exception as e:
        print(f"处理 {ip} 时出错: {str(e)}")
        failed_ips.append(ip)

    finally:
        global completed_count
        completed_count += 1
        print(f"已执行 {completed_count}/{total_count} 个IP。")


def parse_interface_config(config_text):
    pattern = re.compile(r"""
        interface\s+(\S+)               # 提取接口名称
        (.*?)                            # 提取接口配置的所有内容
        \#                               # 匹配结束符号
    """, re.DOTALL | re.VERBOSE)

    results = []
    matches = pattern.findall(config_text)

    for interface, details in matches:
        # 只匹配特定类型的接口
        if not re.match(r'^(GigabitEthernet|10GE|25GE)', interface):
            continue

        port_info = {"Port": interface}

        # 提取描述
        description_match = re.search(r'description\s+(.+)', details)
        port_info["Description"] = description_match.group(1) if description_match else "NA"

        # 提取 negotiation 配置
        port_info["Negotiation"] = (
            "negotiation disable" if "negotiation disable" in details else
            "undo negotiation auto" if "undo negotiation auto" in details else
            "NA"
        )

        # 提取 link-type
        link_type_match = re.search(r'port link-type\s+(\S+)', details)
        port_info["LinkType"] = link_type_match.group(1) if link_type_match else "NA"

        # 合并 DefaultVLAN 和 TrunkVLANs为一个字段 VLAN
        vlans = []

        # 提取 DefaultVLAN
        default_vlan_match = re.search(r'port default vlan\s+(\S+)', details)
        if default_vlan_match:
            vlans.append(default_vlan_match.group(1))

        # 提取 TrunkVLANs，确保忽略 undo 行
        trunk_vlan_matches = re.findall(r'port trunk allow-pass vlan\s+([^\n]+)', details)
        for match in trunk_vlan_matches:
            if match:
                vlans.extend(match.split())

        # 合并 VLANs 为一个字符串
        port_info["VLAN"] = " ".join(vlans).strip() if vlans else "NA"

        # 去掉 VLAN 中的单独数字 1
        port_info["VLAN"] = " ".join(vlan for vlan in port_info["VLAN"].split() if vlan != "1")

        # 提取 speed 配置
        speed_match = re.search(r'speed\s+(\S+)', details)
        port_info["Speed"] = speed_match.group(1) if speed_match else "NA"

        results.append(port_info)

    return results


# 初始化连接池
with ThreadPoolExecutor() as executor:
    # 提交每个IP的处理任务给线程池
    process_futures = [executor.submit(process_ip, ip) for ip in ip_list]

    # 等待所有任务完成
    for future in as_completed(process_futures):
        future.result()

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
datetime_str = current_datetime.strftime("%Y%m%d")

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 构建结果保存路径
output_folder = os.path.join(desktop_path, "output_folder")
os.makedirs(output_folder, exist_ok=True)
filename = f"Port_config_{datetime_str}.xlsx"
output_file = os.path.join(output_folder, filename)

# 将结果保存到表格
df = pd.DataFrame(results)
df.to_excel(output_file, index=False)

print(f"结果已保存到文件: {output_file}")
print(f"已完成IP列表: {completed_count}/{total_count}")
print(f"未完成IP列表: {failed_ips}")


