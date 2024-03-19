# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

sw1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.110',
    'username': 'pccw2023',
    'password': 'P@ssw0rd',
}

acl_template = '''
acl number 2002
{% for ip in allow_ip %}
  rule permit source {{ ip }} 0
{% endfor %}
{% for ip in disallow_ip %}
  rule deny source {{ ip }} 0
{% endfor %}
interface {{ interface }}
  ip address 192.168.1.101 255.255.255.0
  description test101
'''

allow_ip = ['10.1.10.1', '10.1.10.2']
disallow_ip = ['10.1.10.3', '10.1.10.4']
interface = 'Loopback1'

loader = FileSystemLoader('..')
environment = Environment(loader=loader)
tpl = environment.from_string(acl_template)

acl_config = tpl.render(allow_ip=allow_ip, disallow_ip=disallow_ip, interface=interface)

with open("ssh.acl.config.txt", "w") as f:
    f.write(acl_config)

with ConnectHandler(**sw1) as conn:
    print("已经成功登录交换机" + sw1['ip'])
    output = conn.send_config_from_file("ssh.acl.config.txt")
    print(output)

