import re

interface_data = """
Interface                   IP Address/Mask    Physical Protocol VPN           
10GE1/0/7                   172.17.193.193/29  up       up       --            
10GE2/0/7                   unassigned         down     down     --            
Eth-Trunk36                 192.168.14.97/29   up       up       FI-MON        
LoopBack1                   172.17.191.1/32    up       up(s)    --            
MEth0/0/0                   unassigned         down     down     --            
NULL0                       unassigned         up       up(s)    --            
Vlanif108                   172.16.208.29/28   up       up       --            
Vlanif401                   172.17.215.1/24    *down    down     --            
Vlanif570                   172.17.191.129/25  up       up       --            
Vlanif572                   192.168.14.81/29   up       up       FI-MON        
Vlanif573                   192.168.14.1/26    up       up       FI-MON        
Vlanif574                   172.17.187.1/27    up       up       --            
Vlanif575                   172.17.187.33/27   up       up       --            
Vlanif576                   172.17.191.17/29   up       up       --            
Vlanif577                   172.17.191.25/29   up       up       --            
Vlanif906                   172.17.209.57/29   *down    down     --            
Vlanif908                   172.17.208.18/28   up       up       -- 
"""

ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', interface_data)
print(ip_addresses)