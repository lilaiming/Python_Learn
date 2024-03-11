# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

# >号模式下处理提示符
# with ConnectHandler(**sw1) as connect:
#     print("已经成功登录交换机" + sw1['ip'])
#
#     # 发送命令并处理交互式提示
#     output = connect.send_command_timing(command_string="save",
#                                          strip_prompt=False,
#                                          strip_command=False)
#
#     # 检查是否存在提示符
#     if 'continue?[Y/N]' in output:
#         # 输入指定的响应（这里是输入Y）
#         output += connect.send_command_timing(command_string="Y",
#                                               strip_prompt=False,
#                                               strip_command=False)
#
#     print(output)


# 配置模式下处理提示符

with ConnectHandler(**sw1) as connect:
    print("已经成功登录交换机" + sw1['ip'])

    connect.config_mode()

    # 发送命令并处理交互式提示
    output = connect.send_command_timing(command_string="snmp-agent trap enable",
                                         strip_prompt=False,
                                         strip_command=False)

    # 检查是否存在提示符
    if 'Continue? [Y/N]:' in output:
        # 输入指定的响应（这里是输入Y）
        output += connect.send_command_timing(command_string="Y",
                                              strip_prompt=False,
                                              strip_command=False)

    print(output)