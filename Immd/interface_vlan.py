# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 定义原始配置
config = """

#
interface Eth-Trunk21
 ip netstream inbound
 ip netstream outbound
 ip netstream sampler fix-packets 1024 inbound
 ip netstream sampler fix-packets 1024 outbound
 statistic enable
#
interface Eth-Trunk21.902 mode l2
 statistic enable mode single
 encapsulation dot1q vid 902
 rewrite pop single
 bridge-domain 902
 ip netstream inbound
 ip netstream outbound
 ip netstream sampler fix-packets 1024 inbound
 ip netstream sampler fix-packets 1024 outbound
#

"""

# 处理配置
lines = config.strip().split('\n')
output = []
for line in lines:
    if line.startswith("interface"):
        output.append(line)
        # output.append(" statistics enable")
        output.append(" statistic enable mode single")
        # output.append(" statistic ip enable inbound")
        # output.append(" statistic ip enable outbound")
        output.append("#")
# 生成新的配置
new_config = '\n'.join(output)

# 打印新的配置
print("#")
print(new_config)


