# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os

template_text = """

bridge-domain xxx
vxlan vni 140xxx split-horizon-mode
evpn binding vpn-instance MCN_DEV bd-tag xxx
#
interface Eth-Trunk 100.xxx mode l2
encapsulation dot1q vid xxx
rewrite pop single
bridge-domain xxx
#
interface Nve1
vni 140xxx head-end peer-list protocol bgp
"""

numbers = ['100', '101', '102', '103']

output_file = "D:/OneDrive - Lenovo/Python/openfile/evpn_vxlan_no.txt"

with open(output_file, 'w') as file:
    for number in numbers:
        replaced_text = template_text.replace('xxx', number)
        file.write(replaced_text)
        file.write('-'*50 + '\n')
