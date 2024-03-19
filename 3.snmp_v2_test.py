# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from pysnmp.hlapi import *

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
        print(f"SNMP v2 测试失败：{errorIndication}")
    elif errorStatus:
        print(f"SNMP v2 测试失败：{errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"SNMP v2 测试成功：{varBinds[0][1].prettyPrint()}")
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


# 测试SNMP v2
ip = '192.168.56.10'
community = 'P@ssw0rd'
test_snmp_v2(ip, community)


