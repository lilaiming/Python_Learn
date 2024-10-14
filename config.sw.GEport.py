# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 原始数据
data = """
1/0/5	OCNHQSLBDZ01: OB/MGMT	Access	222	1000
1/0/6	OCNHQSLBDZ01: OB/1.0	Trunk	225	1000
1/0/7	OCNHQSXHVM11: OB/1	Access	225	1000
1/0/8	OCNHQSXHVM11: OB/iDRAC	Access	225	1000
2/0/3	OCNHQSLBDZ01: OB/2	Trunk	225	1000
2/0/4	OCNHQSXHVM11: PCI1/1	Access	225	1000
2/0/5	OCNHQSTLDZ01: OB/1	Access	225	1000
"""

# 定义模板
template = """
interface GigabitEthernet {interface}
 description To_{description}
 port link-type access
 port default vlan {vlan}
 undo negotiation auto
 speed {speed}
 undo lldp enable
#
"""

# 处理每一行数据
for line in data.strip().split('\n'):
    parts = line.split()

    # 提取各个字段
    interface = parts[0]
    description = " ".join(parts[1:-2])  # 合并中间的描述部分
    speed = parts[-1]
    vlan = parts[-2]

    # 生成配置
    config = template.format(interface=interface, description=description, vlan=vlan, speed=speed)

    # 输出配置
    print(config.strip())  # 使用 strip() 去掉多余的空行












