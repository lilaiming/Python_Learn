# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

# 定义原始配置
config = """

#
interface Eth-Trunk1
 description To_DEV-CIG
 port default vlan 123
 mode lacp-static
 dfs-group 1 m-lag 1
#
interface Eth-Trunk2
 description To_DEV-GNET
 port default vlan 198
 mode lacp-static
 dfs-group 1 m-lag 2
#
interface Eth-Trunk3
 description ITPNHQFCRZ01-Eth9(Bond0)
 port default vlan 160
 stp edged-port enable
#
interface Eth-Trunk4
 description ANVNHQFCUZ01-Eth8(Bond1)
 port default vlan 161
 stp edged-port enable
#
interface Eth-Trunk8
 undo portswitch
 description Keepalive
 ip binding vpn-instance GNET
 ip address 10.26.13.249 255.255.255.252
 mode lacp-static
#
interface Eth-Trunk9
 undo portswitch
 description M-LAG Keepalive
 ip binding vpn-instance mlag-keepalive
 ip address 192.168.100.1 255.255.255.252
 mode lacp-static
#
interface Eth-Trunk10
 description M-LAG Peer-Link
 mode lacp-static
 peer-link 1
 port vlan exclude 1 
#
interface Eth-Trunk11
 description To_ANVNHQFWUD01
 port default vlan 123
 mode lacp-static
 dfs-group 1 m-lag 11
 port-mirroring observe-port 1 inbound
 port-mirroring observe-port 1 outbound
#
interface Eth-Trunk12
 description To_ANVNHQFWUD01
 port default vlan 198
 mode lacp-static
 dfs-group 1 m-lag 12
 port-mirroring observe-port 1 inbound
 port-mirroring observe-port 1 outbound
#
interface Eth-Trunk13
 description To_ANVNHQFWUD01
 port default vlan 199
 mode lacp-static
 dfs-group 1 m-lag 13
 port-mirroring observe-port 1 inbound
 port-mirroring observe-port 1 outbound
#
interface Eth-Trunk24
 description To_ANVNHQSBTZ01C01
 port link-type trunk
 undo port trunk allow-pass vlan 1
 port trunk allow-pass vlan 122 126 141 to 142 160 to 162 198 to 199 241 351 to 355 429 493 618
 mode lacp-static
 dfs-group 1 m-lag 24
#
interface Eth-Trunk46
 description To_DEV-Ext_Party
 port default vlan 199
 mode lacp-static
 dfs-group 1 m-lag 46
#
interface Eth-Trunk101
 description To_ANVNHQSBUZ11M21
 port link-type trunk
 undo port trunk allow-pass vlan 1
 port trunk allow-pass vlan 141 to 142 160 to 162 199 241 351 to 355 429
 mode lacp-static
 dfs-group 1 m-lag 101
#
interface Eth-Trunk102
 description To_ANVNHQSBUZ11M11
 port link-type trunk
 undo port trunk allow-pass vlan 1
 port trunk allow-pass vlan 141 to 142 160 to 162 241 351 to 355 429
 mode lacp-static
 dfs-group 1 m-lag 102
#
interface Eth-Trunk103
 description To_ANVNHQSBUZ11M31
 port link-type trunk
 undo port trunk allow-pass vlan 1
 port trunk allow-pass vlan 141 to 142 160 to 162 241 351 to 355 429
 mode lacp-static
 dfs-group 1 m-lag 103
#
interface Eth-Trunk104
 description To_ANVNHQSBUZ11M41
 port link-type trunk
 undo port trunk allow-pass vlan 1
 port trunk allow-pass vlan 141 to 142 160 to 162 241 351 to 355 429
 mode lacp-static
 dfs-group 1 m-lag 104
#

"""

# 处理配置
lines = config.strip().split('\n')
output = []
for line in lines:
    if line.startswith("interface"):
        output.append(line)
        output.append(" undo netstream inbound ip")
        output.append(" undo netstream outbound ip")
        output.append("#")
# 生成新的配置
new_config = '\n'.join(output)

# 打印新的配置
print("#")
print("#")
print(new_config)
print("#")




