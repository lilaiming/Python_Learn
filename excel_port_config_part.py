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
    """生成仅包含 undo negotiation disable 的配置内容"""
    negotiation_config = ""

    # 根据插槽类型设置 negotiation 配置
    if "10GE" in row["Slot"]:
        negotiation_config = "undo negotiation disable"  # 在10GE模板中配置
    elif "GE" in row["Slot"]:
        negotiation_config = "negotiation auto"  # 在GE模板中配置

    return {
        "NegotiationConfig": negotiation_config,
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
            "B-end Information"
        ]

        # 提取所需的列
        extracted_data = df[columns_to_extract].fillna("").astype(str)

        # 配置模板
        templates = {
            "10GE": (
                "#\n"
                "interface 10GE {Port}\n"
                " description To_{Description}\n"
                " {NegotiationConfig}\n"  # 仅保留 negotiation 配置
                "#\n"
            ),
            "GE": (
                "#\n"
                "interface GigabitEthernet {Port}\n"
                " description To_{Description}\n"
                " {NegotiationConfig}\n"  # 仅保留 negotiation 配置
                "#\n"
            )
        }

        # 遍历每一行数据，生成配置并保存
        for _, row in extracted_data.iterrows():
            hostname = row["A End Hostname"].replace('/', '_').replace('\\', '_')  # 替换无效字符
            slot = row["Slot"]
            template = templates.get(
                "10GE" if "10GE" in slot else "GE" if "GE" in slot else None)

            if template is None:
                print(f"未匹配到模板，Slot: {slot}")
                continue

            config_data = generate_config(row)
            config = template.format(
                Port=row["Port"],
                Description=row["B-end Information"],
                NegotiationConfig=config_data["NegotiationConfig"]
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