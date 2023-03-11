# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import random #导入random模块

#随机产生IP地址四个段落的数字
section1 = random.randint(1,255)
section2 = random.randint(1,255)
section3 = random.randint(1,255)
section4 = random.randint(1,255)

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
#要把数字转换成字符串，并具拼接在一起！大家可以想象不转换的结果是什么？
print(random_ip)
#打印结果
