# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


print('welcome to qytang!')
print('welcome to lenovo!')
print('welcome to python!')
print('github commit 1')
print('github commit 2')

def panduan(a,b) :
    if a == b :
        qq= "a=b"
    elif a > b :
        qq= "a>b"
    elif a < b :
        qq= "a<b"
    else:
        print ('Error')
    return qq
x = panduan(8,7)
print(x)


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


























