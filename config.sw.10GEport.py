# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 原始数据
data = """

1/0/1	APNHQSWSKM41: OB1/1	334	1000
1/0/2	APNHQSWSKM41: OB1/2	960	1000
1/0/3	APNHQSWSKM41: OB/iLO	960	1000
1/0/6	APNHQSXHVM41: OB/iLO	960	1000
1/0/9	APNHQSWSBK41: OB1/1	962	1000
1/0/10	APNHQSWSBK41: OB1/2	960	1000
1/0/11	APNHQSWSBK41: OB/iLO	960	1000

"""

# 定义access模板
template = """
interface 10GE {interface}
 description To_{description}
 port link-type access
 port default vlan {vlan}
 negotiation disable
 speed {speed}
 lldp disable
#
"""

# 定义trunk模板
# template = """
# interface 10GE {interface}
#  description To_{description}
#  port link-type trunk
#  port trunk allow-pass vlan {vlan}
#  undo port trunk allow-pass vlan 1
#  undo stp edged-port enable
#  negotiation disable
#  speed {speed}
# #
# """

# 处理每一行数据
for line in data.strip().split('\n'):
    parts = line.split()

    # 提取各个字段
    interface = parts[0]
    description = " ".join(parts[1:3])  # 合并中间的描述部分
    speed = parts[-1]
    vlan = " ".join(parts[3:-1])

    # 生成配置
    config = template.format(interface=interface, description=description, vlan=vlan, speed=speed)

    # 输出配置
    print(config.strip())  # 使用 strip() 去掉多余的空行












