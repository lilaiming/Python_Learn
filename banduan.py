# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

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
x = panduan(3,6)
print(x)

