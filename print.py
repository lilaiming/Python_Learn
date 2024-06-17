import re

output_License = """
MainBoard:ve license    : flash:/LICQPZQ1R527HA_102358553719.dat
 License state     : Normal
 Revoke ticket     : No ticket
 
 No relevant customer information
 
 Product name      : S6700
 Product version   : all
 Licen : LIC20230601CYKJ60
 Creator           : Huawei Technologies Co., Ltd.
 Created Time      : 2023-06-01 16:18:32
 Feature name      : ES6FEA1
 Authorize type    : COMM
 Expired date      : PERMANENT
 Trial days        : --

"""

pattern = r" License Serial No :\s*(\w+)"
matches = re.search(pattern, output_License)
if matches:
    License = matches.group(1)
else:
    License = "No license"

print(License)
