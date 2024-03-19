# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from pysnmp.hlapi import *

# 测试SNMP v3
def test_snmp_v3(ip, username, auth_password, priv_password, auth_protocol='sha', priv_protocol='aes256'):
    auth_protocol_map = {
        'md5': usmHMACMD5AuthProtocol,
        'sha': usmHMACSHAAuthProtocol
    }
    priv_protocol_map = {
        'des': usmDESPrivProtocol,
        'aes128': usmAesCfb128Protocol,
        'aes192': usmAesCfb192Protocol,
        'aes256': usmAesCfb256Protocol
    }

    auth_protocol = auth_protocol_map.get(auth_protocol, usmHMACSHAAuthProtocol)
    priv_protocol = priv_protocol_map.get(priv_protocol, usmAesCfb256Protocol)

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               UsmUserData(
                   userName=username,
                   authKey=auth_password,
                   privKey=priv_password,
                   authProtocol=auth_protocol,
                   privProtocol=priv_protocol
               ),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if errorIndication:
        print(f"SNMP v3 测试失败：{errorIndication}")
    elif errorStatus:
        print(f"SNMP v3 测试失败：{errorStatus.prettyPrint()} at {errorIndex}")
    else:
        print(f"SNMP v3 测试成功：{varBinds[0][1].prettyPrint()}")
        # 获取设备名称
        get_device_name(ip, username, auth_password, priv_password, auth_protocol, priv_protocol)


# 获取设备名称
def get_device_name(ip, username, auth_password, priv_password, auth_protocol, priv_protocol):
    auth_protocol_map = {
        'md5': usmHMACMD5AuthProtocol,
        'sha': usmHMACSHAAuthProtocol
    }
    priv_protocol_map = {
        'des': usmDESPrivProtocol,
        'aes128': usmAesCfb128Protocol,
        'aes192': usmAesCfb192Protocol,
        'aes256': usmAesCfb256Protocol
    }

    auth_protocol = auth_protocol_map.get(auth_protocol, usmHMACSHAAuthProtocol)
    priv_protocol = priv_protocol_map.get(priv_protocol, usmAesCfb256Protocol)

    target = UdpTransportTarget((ip, 161))
    auth_data = UsmUserData(
        userName=username,
        authKey=auth_password,
        privKey=priv_password,
        authProtocol=auth_protocol,
        privProtocol=priv_protocol
    )

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


# 测试SNMP v3
ip = '192.168.56.10'
username = 'snmp_immd'
auth_password = 'P@ssw0rd'
priv_password = 'P@ssw0rd'
auth_protocol = 'sha'  # 认证协议，可选值为 'md5' 或 'sha'
priv_protocol = 'aes256'  # 加密协议，可选值为 'des', 'aes128', 'aes192' 或 'aes256'
test_snmp_v3(ip, username, auth_password, priv_password, auth_protocol, priv_protocol)
