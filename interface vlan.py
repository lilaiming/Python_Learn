# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

data = [
    "911 MCN-DW2-UAT-User 172.17.206.0 26",
    "912 MCN-DW2-Svr 172.17.206.64 26   ",
    "913 MCN-DW2-Mgmt 172.17.206.128 26"

]

for item in data:
    parts = item.split()  # 拆分每一行数据
    vlan = parts[0]  # VLAN号
    description = ' '.join(parts[1:-2])  # 描述，将剩余部分拼接起来
    ip_address = parts[-2]  # IP地址
    subnet_mask = parts[-1]  # 子网掩码

    # 将IP地址的最后一个数加1
    ip_parts = ip_address.split('.')
    ip_parts[-1] = str(int(ip_parts[-1]) + 1)
    updated_ip_address = '.'.join(ip_parts)

    print('#')  # 打印#以分隔每个配置
    print(f"interface Vlanif {vlan}")
    print(f" description {description}")
    print(" shutdown")  # 设置接口为关闭状态
    print(f" ip address {updated_ip_address} {subnet_mask}")
    print(" ospf enable 172 area 0.0.0.0")

