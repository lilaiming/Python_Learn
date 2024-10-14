import pandas as pd
import os

# 定义文件路径
desktop_path = os.path.expanduser("~/Desktop/output_folder")
file_name = "PDCAS(non-PROD).xlsx"
file_path = os.path.join(desktop_path, file_name)

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

# 读取 Excel 文件
try:
    # 读取特定工作表 "Port mapping (IP)"
    df = pd.read_excel(file_path, sheet_name="Port mapping (IP)")

    # 提取所需的列
    extracted_data = df[columns_to_extract]

    # 配置模板
    templates = {
        "10GE": (
            "#\n"
            "interface 10GE {Port}\n"
            " description To_{Description}\n"
            " {LinkType}\n"
            " {VLANConfig}\n"
            " {NegotiationConfig}\n"  # 将 negotiation 配置放在这里
            " {SpeedConfig}\n"  # 将速度配置放在这里
            "#\n"
        ),
        "25GE": (
            "#\n"
            "interface 25GE {Port}\n"
            " description To_{Description}\n"
            " {LinkType}\n"
            " {VLANConfig}\n"
            "#\n"  # 不包含 SpeedConfig
        ),
        "GE": (
            "#\n"
            "interface GigabitEthernet {Port}\n"
            " description To_{Description}\n"
            " {LinkType}\n"
            " {VLANConfig}\n"
            " {NegotiationConfig}\n"  # 将 negotiation 配置放在这里
            " {SpeedConfig}\n"  # 将速度配置放在这里
            "#\n"
        )
    }

    # 遍历每一行数据，生成配置并保存
    for index, row in extracted_data.iterrows():
        a_end_hostname = row["A End Hostname"].replace('/', '_').replace('\\', '_')  # 替换无效字符
        output_file_name = f"{a_end_hostname}.txt"  # 使用“A End Hostname”作为文件名
        output_file_path = os.path.join(desktop_path, output_file_name)

        # 根据 Slot 选择模板
        slot = row["Slot"]
        if "10GE" in slot:
            template = templates["10GE"]
        elif "25GE" in slot:
            template = templates["25GE"]
        elif "GE" in slot:
            template = templates["GE"]
        else:
            print(f"未匹配到模板，Slot: {slot}")
            continue

        # 根据 "Access / Trunk Mode" 列确定 link-type 和 VLAN 配置
        access_mode = row["Access / Trunk Mode"]
        if access_mode == "Access":
            link_type = "port link-type access"
            vlan_config = f"port default vlan {row['VLAN no']}"  # 保留这行
        elif access_mode == "Trunk":
            link_type = "port link-type trunk"
            vlan_config = (
                f"undo port trunk allow-pass vlan 1\n"
                f" port trunk allow-pass vlan {row['VLAN no']}"  # 添加两行
            )
        else:
            link_type = ""
            vlan_config = ""

        # 根据 Speed 列处理速度配置
        speed_value = row["Speed(100M/1G/10G/Auto)"]
        if speed_value == "Auto":
            speed_config = ""  # 不配置 {SpeedConfig}
            negotiation_config = ""  # 不配置 negotiation 行
        elif speed_value == "10G":
            speed_config = "speed 10000"
            negotiation_config = "negotiation disable"  # 只在10GE模板中加
        else:
            speed_config = f"speed {speed_value}"
            negotiation_config = "undo negotiation auto"  # 只在GE模板中加

        # 生成配置内容
        config = template.format(
            Port=row["Port"],
            Description=row["B-end Information"],
            LinkType=link_type,
            VLANConfig=vlan_config,
            NegotiationConfig=negotiation_config if negotiation_config else "",  # 处理空值
            SpeedConfig=speed_config if speed_config else ""  # 处理空值
        )

        # 以追加模式打开文件
        with open(output_file_path, 'a', encoding='utf-8') as file:
            file.write(config)  # 写入生成的配置内容

        print(f"配置已成功保存到: {a_end_hostname}")  # 修改为只显示文件名

except FileNotFoundError:
    print(f"文件未找到: {file_path}. 请确认文件路径和文件名。")
except ValueError as ve:
    print(f"发生错误: {ve}. 请确认工作表名称是否正确。")
except Exception as e:
    print(f"发生错误: {e}. 请检查文件格式和内容。")