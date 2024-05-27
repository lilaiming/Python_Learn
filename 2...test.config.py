# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler

# SSH 连接信息
device = {
    'device_type': 'huawei',
    'ip': '192.168.13.119',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
    'global_delay_factor': 1,  # 增加全局延迟因子
}

# 连接到设备
with ConnectHandler(**device) as conn:
    print(f"成功登录交换机 {device['ip']}")

    # 发送配置命令
    commands = [
        'info-center loghost 1.1.1.3',
        'commit',
    ]
    output = conn.send_config_set(commands)
    # output = conn.send_config_set(commands, exit_config_mode=False)
    print(output)












