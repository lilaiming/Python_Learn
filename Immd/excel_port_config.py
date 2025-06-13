# -*- coding: utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email: essid@qq.com

import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


def select_file():
    """创建一个文件选择对话框"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择 Excel 文件", filetypes=[("Excel files", "*.xlsx;*.xls")])
    return file_path


def generate_config(row):
    """生成配置内容"""
    link_type = "port link-type access" if row["Access / Trunk Mode"] == "Access" else "port link-type trunk"
    vlan_config = f"port default vlan {row['VLAN no']}" if row["Access / Trunk Mode"] == "Access" else f"undo port trunk allow-pass vlan 1\n port trunk allow-pass vlan {row['VLAN no']}"

    # 处理速度配置
    speed_value = row["Speed(100M/1G/10G/Auto)"]

    # 替换速度值
    if speed_value == "10G":
        speed_value = "10000"
    elif speed_value == "1G":
        speed_value = "1000"
    elif speed_value == "a-1000":
        speed_value = "1000"
    elif speed_value == "a-100":
        speed_value = "100"

    speed_config = f"speed {speed_value}" if speed_value != "Auto" else ""

    # 处理 negotiation 配置
    negotiation_config = ""
    if speed_value != "Auto":
        if "10GE" in row["Slot"]:
            negotiation_config = "negotiation disable"  # 在10GE模板中配置
        elif "GE" in row["Slot"]:
            negotiation_config = "undo negotiation auto"  # 在GE模板中配置

    return {
        "LinkType": link_type,
        "VLANConfig": vlan_config,
        "NegotiationConfig": negotiation_config,
        "SpeedConfig": speed_config,
    }


def write_config_to_file(file_path, hostname, config):
    """将生成的配置内容写入文件"""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(config)


def main():
    # 选择文件
    file_path = select_file()
    if not file_path:
        print("未选择文件，程序结束。")
        exit()

    # 读取 Excel 文件
    try:
        df = pd.read_excel(file_path, sheet_name="Port mapping (IP)")
        df.columns = df.columns.str.strip().str.replace('\n', '')  # 处理列名

        # 定义需要提取的列名
        columns_to_extract = [
            "A End Hostname",
            "Slot",
            "Port",
            "B-end Information",
            "Access / Trunk Mode",
            "VLAN no",
            "Speed(100M/1G/10G/Auto)"
        ]

        # 提取所需的列
        extracted_data = df[columns_to_extract].fillna("").astype(str)

        # 配置模板
        templates = {
            "10GE": (
                "#\n"
                "interface 10GE {Port}\n"
                " description To_{Description}\n"
                " {LinkType}\n"
                " {VLANConfig}\n"
                " {NegotiationConfig}\n"  # 将 negotiation 配置放在这里
                " {SpeedConfig}\n"
                "#\n"
            ),
            "25GE": (
                "#\n"
                "interface 25GE {Port}\n"
                " description To_{Description}\n"
                " {LinkType}\n"
                " {VLANConfig}\n"
                "#\n"
            ),
            "GE": (
                "#\n"
                "interface GigabitEthernet {Port}\n"
                " description To_{Description}\n"
                " {LinkType}\n"
                " {VLANConfig}\n"
                " {NegotiationConfig}\n"  # 将 negotiation 配置放在这里
                " {SpeedConfig}\n"
                "#\n"
            )
        }

        # 遍历每一行数据，生成配置并保存
        for _, row in extracted_data.iterrows():
            hostname = row["A End Hostname"].replace('/', '_').replace('\\', '_')  # 替换无效字符
            slot = row["Slot"]
            template = templates.get(
                "10GE" if "10GE" in slot else "25GE" if "25GE" in slot else "GE" if "GE" in slot else None)

            if template is None:
                print(f"未匹配到模板，Slot: {slot}")
                continue

            config_data = generate_config(row)
            config = template.format(
                Port=row["Port"],
                Description=row["B-end Information"],
                LinkType=config_data["LinkType"],
                VLANConfig=config_data["VLANConfig"],
                NegotiationConfig=config_data["NegotiationConfig"],
                SpeedConfig=config_data["SpeedConfig"]
            )

            output_file_name = f"{hostname}.txt"
            output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)  # 保存到同一目录

            write_config_to_file(output_file_path, hostname, config)
            print(f"配置已成功保存到: {hostname}")  # 输出文件名

    except FileNotFoundError:
        print(f"文件未找到: {file_path}. 请确认文件路径和文件名。")
    except ValueError as ve:
        print(f"发生错误: {ve}. 请确认工作表名称是否正确。")
    except Exception as e:
        print(f"发生错误: {e}. 请检查文件格式和内容。")


if __name__ == "__main__":
    main()




