import re

vlan_data = """
                                                            ^
Error: Wrong parameter found at '^' position.
                                                            ^
Error: Wrong parameter found at '^' position.
                                                            ^
Error: Wrong parameter found at '^' position.
                                                            ^
Error: Wrong parameter found at '^' position.
                                                            ^
Error: Wrong parameter found at '^' position.
                                                            ^
Error: Wrong parameter found at '^' position.
                                                      ^
Error: Wrong parameter found at '^' position.
                                                      ^
Error: Wrong parameter found at '^' position.
2024-06-25 14:06:15.411 +08:00
#
interface MEth0/0/0
 ip binding vpn-instance mgmt
 ip address 10.26.169.226 255.255.255.192
#
return
"""

ip_match = re.search(r"ip address (\S+)", vlan_data)
if ip_match:
    MGMT = ip_match.group(1)
    print(MGMT)