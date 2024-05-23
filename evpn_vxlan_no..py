# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import os

template_text = """

bridge-domain xxx
vxlan vni 110xxx split-horizon-mode
evpn binding vpn-instance AN_DEV bd-tag xxx
#
interface Eth-Trunk 200.xxx mode l2
encapsulation dot1q vid xxx
rewrite pop single
bridge-domain xxx
#
interface Nve1
vni 110xxx head-end peer-list protocol bgp
"""


list2 =[]
list=[141,142]

for i in list:
    str(i)
    list2.append( str(i))
print(list2)


output_file = "C:/Users/lilm6/Desktop/output_folder/evpn_vxlan_no.txt"

with open(output_file, 'w') as file:
    for number in list2:
        replaced_text = template_text.replace('xxx', number)
        file.write(replaced_text)
        file.write('-'*50 + '\n')
        print(replaced_text)
        print('-'*50 + '\n')




