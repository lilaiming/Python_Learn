# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from pysnmp.hlapi import *
from concurrent.futures import ThreadPoolExecutor

# 从文件中读取IP地址列表
def read_ip_list(filename):
    with open(filename, 'r') as file:
        ip_list = file.read().splitlines()
    return ip_list

# 测试SNMP v2
def test_snmp_v2(ip, community):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community, mpModel=1),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if errorIndication:
        print(f"{ip} SNMP v2 测试失败：- {errorIndication}")
    elif errorStatus:
        print(f"{ip} SNMP v2 测试失败：- {errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"{ip} SNMP v2 测试成功：")
        # print(f"SNMP v2 测试成功：{ip} - {varBinds[0][1].prettyPrint()}")
        # 获取设备名称
        get_device_name(ip, community)


# 获取设备名称
def get_device_name(ip, community):
    target = UdpTransportTarget((ip, 161))
    auth_data = CommunityData(community, mpModel=1)

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               auth_data,
               target,
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)))
    )

    if errorIndication:
        print(f"获取设备名称失败：{errorIndication}")
    elif errorStatus:
        print(f"获取设备名称失败：{errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"设备名称：{varBinds[0][1].prettyPrint()}")


# 读取IP地址列表文件
ip_list = read_ip_list('2.ip_list.txt')

# 使用多线程处理每个IP地址
with ThreadPoolExecutor(max_workers=5) as executor:
    for ip in ip_list:
        community = 'Password'  # 输入交换机配置的community
        executor.submit(test_snmp_v2, ip, community)

# 交换机配置：
# snmp-agent
# snmp-agent trap enable
# snmp-agent sys-info version v2c
# snmp-agent community read cipher Password

