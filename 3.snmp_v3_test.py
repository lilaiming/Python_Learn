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

# 测试SNMP v3
def test_snmp_v3(ip, username, auth_protocol, auth_password, priv_protocol, priv_password):
    target = UdpTransportTarget((ip, 161))
    user = UsmUserData(userName=username,
                       authProtocol=auth_protocol,
                       authKey=auth_password,
                       privProtocol=priv_protocol,
                       privKey=priv_password)
    oid = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))

    errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(), user, target, ContextData(), oid))

    if errorIndication:
        print(f"{ip} SNMP v3 测试失败：- {errorIndication}")
    elif errorStatus:
        print(f"{ip} SNMP v3 测试失败：- {errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"{ip} SNMP v3 测试成功：")
        # print(f"SNMP v3 测试成功：{ip} - {varBinds[0][1].prettyPrint()}")

# 获取设备名称
def get_device_name(ip, username, auth_protocol, auth_password, priv_protocol, priv_password):
    target = UdpTransportTarget((ip, 161))
    user = UsmUserData(userName=username,
                       authProtocol=auth_protocol,
                       authKey=auth_password,
                       privProtocol=priv_protocol,
                       privKey=priv_password)
    oid = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0))

    errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(), user, target, ContextData(), oid))

    if errorIndication:
        print(f"获取设备名称失败： {errorIndication}")
    elif errorStatus:
        print(f"获取设备名称失败： {errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"设备名称： {varBinds[0][1].prettyPrint()}")

# 读取IP地址列表文件
ip_list = read_ip_list('2.ip_list.txt')

# SNMP v3 配置信息
username = 'snmp_immd'
auth_password = 'Password'
priv_password = 'Password'
auth_protocol = usmHMACSHAAuthProtocol
priv_protocol = usmDESPrivProtocol
# auth_protocol = usmHMACSHA2-256AuthProtocol
# auth_protocol = usmHMACSHA2-512AuthProtocol
# priv_protocol = usmAesCfb256Protocol

# 使用多线程处理每个IP地址
with ThreadPoolExecutor(max_workers=5) as executor:
    for ip in ip_list:
        executor.submit(test_snmp_v3, ip, username, auth_protocol, auth_password, priv_protocol, priv_password)
        executor.submit(get_device_name, ip, username, auth_protocol, auth_password, priv_protocol, priv_password)



#
# S5700交换机配置
# snmp-agent
# snmp-agent trap enable
# snmp-agent sys-info version v3
# snmp-agent group v3 snmp_immd authentication
# snmp-agent group v3 snmp_immd privacy  read-view iso write-view iso notify-view iso
# snmp-agent mib-view included iso iso
# snmp-agent usm-user v3 snmp_immd snmp_immd cipher authentication-mode sha Password privacy-mode des56 Password
##

#
# CE12800交换机配置
# snmp-agent
# snmp-agent trap enable
# snmp-agent sys-info version v3
# snmp-agent group v3 snmp_immd authentication
# snmp-agent mib-view included iso iso
# snmp-agent usm-user v3 snmp_immd
# snmp-agent usm-user v3 snmp_immd group snmp_immd
# snmp-agent usm-user v3 snmp_immd authentication-mode sha
# Password
# Password
# snmp-agent usm-user v3 snmp_immd privacy-mode des56
# Password
# Password
# #