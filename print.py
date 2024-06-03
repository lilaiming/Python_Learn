# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

#
# print('welcome to qytang!')
# print('welcome to lenovo!')
# print('welcome to python!')
# print('github commit 1')
# print('github commit 2')
#
# def panduan(a,b) :
#     if a == b :
#         qq= "a=b"
#     elif a > b :
#         qq= "a>b"
#     elif a < b :
#         qq= "a<b"
#     else:
#         print ('Error')
#     return qq
# x = panduan(8,7)
# print(x)
#
#
# import random #导入random模块
#
# #随机产生IP地址四个段落的数字
# section1 = random.randint(1,255)
# section2 = random.randint(1,255)
# section3 = random.randint(1,255)
# section4 = random.randint(1,255)
#
# random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
# #要把数字转换成字符串，并具拼接在一起！大家可以想象不转换的结果是什么？
# print(random_ip)
# #打印结果
#


#
# import re
#
# string = "Amazon.com: Apple iPhone 13 Pro, 128GB, Alpine Green - Unlocked (Renewed) : Cell Phones & Accessories"
#
# # 使用正则表达式提取字段
# pattern = r":\s(.*?),"
# result = re.search(pattern, string)
#
# if result:
#     extracted_field = result.group(1)
#     print(extracted_field)
#


#
# import os
# import pandas as pd
# from datetime import datetime
#
# # 获取当前日期和星期几
# current_date = datetime.now().date()
# current_day = datetime.now().strftime("%A")
#
# print(current_date)
# print(current_day)
#

#
# import requests  # 导入requests库，用于发送HTTP请求
# import os  # 导入os库，用于文件路径操作
# import re  # 导入re库，用于正则表达式匹配
# import pandas as pd  # 导入pandas库，用于处理和操作数据
# from datetime import datetime  # 导入datetime库，用于日期时间相关操作
#
# Title = 'Apple iPhone 13 Pro'
# price = 496.0
# stock = 2
#
# # 获取当前日期和星期
# current_date = datetime.now()
# current_week = datetime.now().strftime("%A")
# print(current_date)
# print(current_week)
#
#
#
#  # 创建或加载现有的Excel文件
# output_folder = r"C:\Users\lilm6\Desktop\output_folder"
# output_file = os.path.join(output_folder, "amazon_test.xlsx")
#
# if os.path.exists(output_file):
#         df = pd.read_excel(output_file)
# else:
#         df = pd.DataFrame()
#
# if df.empty:
#         last_no = 0
# else:
#         last_no = df["No."].max()
#
#     # 将新数据添加到DataFrame
# new_data = {"No.": last_no + 1, "Date": current_date, "Week": current_week, "Title": Title, "Price": price,"Stock": stock}
# df = df._append(new_data, ignore_index=True)
#
#     # 将DataFrame保存为Excel文件
# df.to_excel(output_file, index=False)
# print("数据保存成功。")
#

#
# import re
#
# string1 = "Hello, lilaiming"
# string2 = "Hello, sign in"
#
# pattern = r"Hello, (.+)"
# match1 = re.match(pattern, string1)
# match2 = re.match(pattern, string2)
#
# if match1:
#     username1 = match1.group(1)
#     print("用户名1:", username1)
# else:
#     print("未找到用户名1")
#
# if match2:
#     username2 = match2.group(1)
#     print("用户名2:", username2)
# else:
#     print("未找到用户名2")
#
# import datetime
#
# # 获取当前日期和时间
# current_datetime = datetime.datetime.now()
#
# # 格式化日期和时间为字符串
# datetime_str = current_datetime.strftime("_%m%d_%Hh%Mm")
#
# # 创建文件名
# filename = f"{datetime_str}.txt"
#
# print(filename)
#


#
# import re
#
# text = """
# Huawei Versatile Routing Platform Software
# VRP (R) software, Version 8.221 (CE6881 V200R022C10SPC500)
# Copyright (C) 2012-2023 Huawei Technologies Co., Ltd.
# HUAWEI CE6881-48T6CQ uptime is 7 days, 23 hours, 28 minutes
# Patch Version: V200R022SPH1b0"""
#
# output_lines_version = text.split('\n')
# version_line = output_lines_version[2]  # 获取第二行
#
#
#
# print(version_line)
# # print("MODEL:", MODEL)
# # print("Version:", version)
#
# import re
#
# version_line = """
# VRP (R) software, Version 5.170 (S5731 V200R022C00SPC500)
# """
#
# pattern = r"Version \d+\.\d+ \((\w+) (V\d+R\d+C\d+SPC\d+)\)"
# matches = re.findall(pattern, version_line)
#
# for match in matches:
#     print(f"{match[0]}")
#     print(f"{match[1]}")
#
# import re
#
# version_line = """
# Huawei Versatile Routing Platform Software
# VRP (R) software, Version 8.221 (CE6881 V200R022C10SPC500)
# Copyright (C) 2012-2023 Huawei Technologies Co., Ltd.
# HUAWEI CE6881-48T6CQ uptime is 8 days, 1 hour, 17 minutes
# Patch Version: V200R022SPH1b0
#
# """
#
# pattern = r"Version \d+\.\d+ \((\w+) (V\d+R\d+C\d+SPC\d+)\)"
# matches = re.search(pattern, version_line)
#
# sss = matches.group(1)
# xxx = matches.group(2)
# print(sss)
# print(xxx)

#
# import re
#
# version_line = """
# Patch Package Name    :flash:/CE6800_V200R022SPH1b0.PAT
# Patch Package Version :V200R022SPH1b0
# Patch Package State   :Running
# Patch Package Run Time:2024-05-22 23:31:36+08:00
# """
#
# pattern = r"Patch Package Version\s*:\s*(V\d+R\d+C\d+SPH\d+[a-zA-Z]\d+)"
# matches = re.search(pattern, version_line)
#
# xxx = matches.group(1)
# #
# # print(xxx)
# #
# import re
#
# data = """
# Patch Package Name    :flash:/CE6800_V200R022SPH1b0.PAT
# Patch Package Version :V200R022SPH1b0
# Patch Package State   :Running
# Patch Package Run Time:2024-05-22 23:31:36+08:00
#
# """
#
# pattern = r"Patch Package Version\s*:\s*(\w+)"
# matches = re.search(pattern, data)
# xxx = matches.group(1)
# print(xxx)
#
#
# import re
#
# data = """
# ESN of slot 1: 102365353525
# ESN of slot 0: 4E2340039806
# """
#
# pattern = r":\s*(.*)"
# matches = re.search(pattern, data)
# print(matches)
# xx = matches.group(1)
# print(xx)
#
import re
#
# data = """
# ----------------------------------------------------------------------------
# Slot       Card   Type               Serial-number            Manu-date
# ----------------------------------------------------------------------------
# backplane  --     CE16804-AH         102365785835             2023-06-08
# 1          --     CEL48XSFD-G        102365916108             2023-06-08
# 2          --     CEL48XSFD-G        102365916115             2023-06-08
# 3          --     CEL36CQFD-G        102365916102             2023-06-08
# 4          --     CEL36CQFD-G        102365916107             2023-06-08
# """
#
# pattern = r"CE16804-AH\s+(\d+)"
# matches = re.search(pattern, data)
# xx = matches.group(1)
# print(xx)
#

#
#
# if Version == "CE16800":
#     output_esn1 = conn.send_command('display esn')
#     pattern = r":\s*(.*)"
#     matches = re.search(pattern, output_esn1)
#     ESN1 = matches.group(1)
#     print(ESN1)
# else:
#     output_esn2 = conn.send_command('display esn')
#     pattern = r"CE16804-AH\s+(\d+)"
#     matches = re.search(pattern, output_esn2)
#     ESN2 = matches.group(1)
#     print(ESN2)
#
#
#
# ttt = """
# Patch Package Version:V200R022SPH1b1
# Patch Package Version :V200R022SPH1b2
# Patch version         :ARV300R022SPH221
# """
#
# pattern =   r"Patch .*[Vv]ersion\s*:\s*(\w+)"
# # pattern = r"Patch Package Version\s*:\s*(\w+)"
# matches = re.findall(pattern, ttt)
# print(matches)



Model = "CE16800"

if Model in ["CE16800", "CE8850EI", "CE6863E", "CE6881"]:
    print("A")
else:
    print("B")









































































































































































































































