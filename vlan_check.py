# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import re
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from collections import defaultdict


def extract_interface_data(file_path):
    """从文件中提取接口数据并识别设备类型"""
    # 正则表达式模式
    hostname_pattern = r'^([A-Za-z0-9]+)-'
    interface_pattern = r'interface\s+(Vlan\w+|Vlanif\d+|Vlan\s*\d+)'
    ip_pattern = r'ip\s+address\s+(\d+\.\d+\.\d+\.\d+\s+\d+\.\d+\.\d+\.\d+)'
    description_pattern = r'description\s+(.+)'
    cisco_pattern = r'ip\s+helper-address\s+168\.106\.128\.21'
    huawei_pattern = r'dhcp\s+relay\s+server-ip\s+168\.106\.128\.21'

    results = []
    hostname_flags = defaultdict(lambda: {"cisco": False, "huawei": False})

    current_hostname = ""
    current_interface = ""
    current_ip = ""
    current_desc = "NA"
    has_ip = False  # 标记当前接口是否有IP地址

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # 移除行尾换行符
                line = line.strip()

                # 跳过空行
                if not line:
                    continue

                # 提取Hostname
                host_match = re.search(hostname_pattern, line)
                if host_match:
                    current_hostname = host_match.group(1)

                # 提取有效配置内容
                if ':' in line:
                    content = line.split(':', 1)[-1].strip()
                elif '-' in line:
                    parts = line.split('-', 2)
                    content = parts[-1].strip() if len(parts) > 2 else line
                else:
                    content = line

                # 检查设备类型特征 - 先于接口检查
                if current_hostname:
                    if re.search(cisco_pattern, content, re.IGNORECASE):
                        hostname_flags[current_hostname]["cisco"] = True
                    if re.search(huawei_pattern, content, re.IGNORECASE):
                        hostname_flags[current_hostname]["huawei"] = True

                # 检查接口配置
                interface_match = re.search(interface_pattern, content, re.IGNORECASE)
                if interface_match:
                    # 保存前一个接口（如果有IP地址）
                    if current_interface and has_ip:
                        results.append({
                            "Hostname": current_hostname,
                            "interface": current_interface,
                            "ip address": current_ip,
                            "description": current_desc
                        })

                    # 开始新接口
                    current_interface = interface_match.group(1).replace(' ', '')
                    current_ip = ""
                    current_desc = "NA"
                    has_ip = False  # 重置IP标记
                    continue

                # 检查IP地址
                ip_match = re.search(ip_pattern, content, re.IGNORECASE)
                if ip_match and current_interface:
                    current_ip = ip_match.group(1)
                    has_ip = True  # 标记有IP地址

                # 检查描述
                desc_match = re.search(description_pattern, content, re.IGNORECASE)
                if desc_match and current_interface:
                    current_desc = desc_match.group(1)

            # 添加最后一个接口（如果有IP地址）
            if current_interface and has_ip:
                results.append({
                    "Hostname": current_hostname,
                    "interface": current_interface,
                    "ip address": current_ip,
                    "description": current_desc
                })

    except Exception as e:
        print(f"处理文件时出错: {str(e)}")

    # 准备Hostname统计表
    hostname_stats = []
    for hostname, flags in hostname_flags.items():
        if flags["cisco"] and flags["huawei"]:
            # 如果同时有Cisco和Huawei特征，则使用更精确的规则
            # 这里可以根据需要进一步优化，目前简单标记为Cisco
            device_type = "Cisco"
        elif flags["cisco"]:
            device_type = "Cisco"
        elif flags["huawei"]:
            device_type = "Huawei"
        else:
            device_type = "未知"
        hostname_stats.append({"Hostname": hostname, "Type": device_type})

    return results, hostname_stats


def main():
    print("请选择日志文件...")

    try:
        # 创建文件选择对话框
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        root.attributes('-topmost', True)  # 确保对话框显示在最前面

        # 选择输入文件
        input_file = filedialog.askopenfilename(
            title="选择日志文件",
            filetypes=[
                ("日志文件", "*.log"),
                ("文本文件", "*.txt"),
                ("配置文件", "*.cfg"),
                ("所有文件", "*.*")
            ]
        )

        if not input_file:
            print("未选择文件，程序退出")
            return

        print(f"已选择文件: {input_file}")

        # 提取数据
        interface_data, hostname_stats = extract_interface_data(input_file)

        # 创建输出文件路径（与输入文件同目录）
        output_dir = os.path.dirname(input_file)
        output_file = os.path.join(output_dir, "接口信息提取结果.xlsx")

        # 创建DataFrame并保存为Excel
        if interface_data or hostname_stats:
            with pd.ExcelWriter(output_file) as writer:
                # 添加接口信息表
                if interface_data:
                    df_interface = pd.DataFrame(interface_data)
                    df_interface = df_interface[["Hostname", "interface", "ip address", "description"]]
                    df_interface.to_excel(writer, sheet_name="接口信息", index=False)

                # 添加Hostname统计表
                if hostname_stats:
                    df_hostname = pd.DataFrame(hostname_stats)
                    df_hostname.to_excel(writer, sheet_name="Hostname统计", index=False)

            print(f"成功提取 {len(interface_data)} 条接口信息")
            print(f"成功统计 {len(hostname_stats)} 个Hostname")
            print(f"结果已保存到: {output_file}")

            # 尝试打开结果文件所在目录
            try:
                os.startfile(output_dir)  # Windows系统
            except:
                print(f"无法自动打开目录，请手动访问: {output_dir}")
        else:
            print("未找到有效的接口信息")
            with open(os.path.join(output_dir, "提取结果.txt"), 'w') as f:
                f.write("未在文件中找到有效的接口配置信息")

    except Exception as e:
        print(f"程序运行时出错: {str(e)}")
        input("按Enter键退出...")


if __name__ == "__main__":
    main()


