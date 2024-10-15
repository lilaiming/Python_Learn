# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

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
            output_sysname = conn.send_command('display current-configuration | include sysname' )
            pattern = r"sysname (.*)"
            matches = re.search(pattern, output_sysname)
            Sysname = matches.group(1)
            # print(Sysname)

            # 获取ZONE,Remark
            if Sysname.startswith("IT"):
                ZONE = "MCN"
                # print(ZONE)
            elif Sysname.startswith("AN"):
                ZONE = "AN"
                # print(ZONE)
            elif Sysname.startswith("DEV"):
                ZONE = "DCI"
                # print(ZONE)
            else:
                ZONE = "-"
                # print(ZONE)
            if Sysname[-4].isdigit() and Sysname[-3] in ["F", "T", "M"]:
                Remark = "access switch"
                # print(Remark)
            elif Sysname[-3] == "C":
                Remark = "core switch"
                # print(Remark)
            elif Sysname[-3] == "D":
                Remark = "distribution switch"
                # print(Remark)
            elif "RT" in Sysname:
                Remark = "router"
                # print(Remark)
            else:
                Remark = "-"
                # print(Remark)

            # 获取MGMT IP
            vlan_interfaces = ['Vlanif162', 'Vlanif262', 'Vlanif362', 'Vlanif570', 'Vlanif883', 'Vlanif1305', 'Ethernet0/0/0', 'GigabitEthernet0/0/8']

            for vlan_interface in vlan_interfaces:
                try:
                    output_vlanif = conn.send_command('display current-configuration interface {}'.format(vlan_interface))
                    # print(output_vlanif)
                    vlan_data = re.search(r"interface {}\n(.+?)#".format(vlan_interface), output_vlanif, re.DOTALL)
                    # print(vlan_data)
                    if vlan_data is None or vlan_data.group(1) == "":
                        continue
                    mlag_match = re.search(r"m-lag ip address (\S+)", vlan_data.group(1))
                    if mlag_match:
                        MGMT = mlag_match.group(1)
                        # print(MGMT)
                    else:
                        ip_match = re.search(r"ip address (\S+)", vlan_data.group(1))
                        if ip_match:
                            MGMT = ip_match.group(1)
                            # print(MGMT)
                        else:
                            continue

                except Exception as e:
                    print("处理 {} 时出错: {}".format(vlan_interface, e))

            # 获取Other IP
            output_other_ip = conn.send_command('display ip interface brief')
            pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
            matches = re.findall(pattern, output_other_ip)
            other_ip = ','.join(matches)
            # print(other_ip)

            # 获取Model和Version
            output_version = conn.send_command('display version')
            pattern = r"Version \d+\.\d+ \((.*) (V\d+R\d+C\d+SPC\d+)\)"
            matches = re.search(pattern, output_version)
            Model = matches.group(1)
            Version = matches.group(2)
            # print(Model)
            # print(Version)

            # 获取Patch
            output_patch = conn.send_command('display patch')
            pattern = r"Patch .*[Vv]ersion\s*:\s*(\w+)"
            matches = re.search(pattern, output_patch)
            Patch = matches.group(1)
            # print(Patch)

            # 获取ESN
            if Model == "CE16800":
                output_esn = conn.send_command('display device manufacture-info')
                pattern = r"CE16804-AH\s+(\d+)"
                matches = re.search(pattern, output_esn)
                ESN = matches.group(1)
                # print(ESN)
            elif Model == "CE5882-48T4S-B":
                output_esn = conn.send_command('display esn')
                pattern = r":\s*(.*)"
                matches = re.findall(pattern, output_esn)
                ESN = ',\n'.join(matches)
                # print(ESN)
            else:
                output_esn = conn.send_command('display esn')
                pattern = r":\s*(.*)"
                matches = re.search(pattern, output_esn)
                ESN = matches.group(1)
                # print(ESN)

            # 获取License
            output_License = conn.send_command('display license')
            pattern = r" License Serial No :\s*(\w+)"
            matches = re.search(pattern, output_License)
            if matches:
                License = matches.group(1)
            else:
                License = "No license"
            # print(License)

            # 存储结果
            results.append({'MCN/AN': ZONE, 'Hostname': Sysname, 'FI-MON IP': ip, 'MGMT IP':MGMT, 'Model':Model, 'Version':Version, 'Patch':Patch, 'ESN':ESN, 'License':License, 'REMARK':Remark, 'Other IP':other_ip})

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



