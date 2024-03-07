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

# numbers = ['306', '347', '400', '401', '419', '420', '421', '422', '423', '424', '425', '429', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '445', '451', '452', '453', '454', '458', '459', '460', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '501', '502', '521', '601', '602', '603', '604', '611', '612', '613', '614', '620', '621', '622', '623', '629', '630', '631', '632', '634', '635', '636', '701', '702', '703']
list2 =[]
list=[306,347,400,401,419,420,421,
422,423,424,425,429,431,432,
433,434,435,436,437,438,439,
440,441,445,451,452,453,454,
458,459,460,467,468,469,470,
471,472,473,474,475,476,477,
478,479,480,483,484,485,486,
487,488,489,490,491,492,493,
494,495,496,497,498,499,501,
502,521,601,602,603,604,611,
612,613,614,620,621,622,623,
629,630,631,632,634,635,636,
701,702,703]
for i in list:
    str(i)
    list2.append( str(i))
print(list2)


output_file = "D:/OneDrive - Lenovo/Python/openfile/evpn_vxlan_no.txt"

with open(output_file, 'w') as file:
    for number in list2:
        replaced_text = template_text.replace('xxx', number)
        file.write(replaced_text)
        file.write('-'*50 + '\n')
        print(replaced_text)
        print('-'*50 + '\n')




