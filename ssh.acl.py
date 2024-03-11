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

loader = FileSystemLoader('templates')
environment = Environment(loader=loader)
tpl = environment.get_template('acl.conf.tpl')

allow_ip = ['10.1.1.1', '10.1.1.2']
disallow_ip = ['10.1.1.3', '10.1.1.4']
out = tpl.render(allow_ip=allow_ip, disallow_ip=disallow_ip, interface='loopback 1')

with open("configuration.conf", "w") as f:
       f.write(out)
       # print(out)
with ConnectHandler(**sw1) as conn:
        print ("已经成功登陆交换机" + sw1['ip'])
        output = conn.send_config_from_file("configuration.conf")
        print (output)




