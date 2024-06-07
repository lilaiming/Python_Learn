# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os

template_text = """

bridge-domain xxx
vxlan vni 140xxx split-horizon-mode
evpn binding vpn-instance MCN_DEV bd-tag xxx
#
interface Eth-Trunk 28.xxx mode l2
encapsulation dot1q vid xxx
rewrite pop single
bridge-domain xxx
#
interface Nve1
vni 140xxx head-end peer-list protocol bgp
"""
# modify vni 110，AN_DEV|MCN_DEV，Eth-Trunk 200.
# modify list vlan no.
list= [
483
]

list2 =[]

for i in list:
    str(i)
    list2.append(str(i))
print(list2)

output_file = "C:/Users/lilm6/Desktop/output_folder/evpn_vxlan_no.txt"

with open(output_file, 'a') as file:
    for number in list2:
        replaced_text = template_text.replace('xxx', number)
        file.write(replaced_text)
        file.write('-'*50 + '\n')
        print(replaced_text)
        print('-'*50 + '\n')




