# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 定义原始配置
config = """

interface Vlanif1315
 description AP2 DEV MCN for Vendors
 ip address 172.17.183.129 255.255.255.128
#
interface Vlanif1399
 description To-FW
 ip address 172.17.191.9 255.255.255.248
#

"""

# 处理配置
lines = config.strip().split('\n')
output = []
for line in lines:
    if line.startswith("interface"):
        output.append(line)
        output.append(" statistics enable")
        output.append("#")
# 生成新的配置
new_config = '\n'.join(output)

# 打印新的配置
print("#")
print(new_config)


