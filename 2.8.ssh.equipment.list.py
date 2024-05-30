# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os
import re
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
            print(Sysname)

            # 获取Model和Version
            output_version = conn.send_command('display version')
            pattern = r"Version \d+\.\d+ \((.*) (V\d+R\d+C\d+SPC\d+)\)"
            matches = re.search(pattern, output_version)
            Model = matches.group(1)
            Version = matches.group(2)
            print(Model)
            print(Version)

            # 获取Patch
            output_patch = conn.send_command('display patch')
            pattern = r"Patch .*[Vv]ersion\s*:\s*(\w+)"
            matches = re.search(pattern, output_patch)
            Patch = matches.group(1)
            print(Patch)

            # 获取ESN
            if Model == "CE16800":
                output_esn = conn.send_command('display device manufacture-info')
                pattern = r"CE16804-AH\s+(\d+)"
                matches = re.search(pattern, output_esn)
                ESN = matches.group(1)
                print(ESN)
            else:
                output_esn = conn.send_command('display esn')
                pattern = r":\s*(.*)"
                matches = re.search(pattern, output_esn)
                ESN = matches.group(1)
                print(ESN)



            # 存储结果
            results.append({'Hostname': Sysname, 'MGMT IP': ip, 'Model':Model, 'Version':Version, 'Patch':Patch, 'ESN':ESN   })

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

# 获取桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 构建结果保存路径
output_folder = os.path.join(desktop_path, "output_folder")
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "DEV_Equipment_List.xlsx")

# 将结果保存到表格
df = pd.DataFrame(results)
df.to_excel(output_file, index=False)

print(f"结果已保存到文件: {output_file}")
print("所有IP执行完成。")
print(f"已完成IP列表: {completed_count}/{total_count}")
print(f"未完成IP列表: {failed_ips}")



