# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import paramiko
import time

ip = "10.109.64.136";user='lenovo';password='Lenovo,!'

ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect(hostname=ip,port=22,username=user,password=password,timeout=5,
             allow_agent=False,look_for_keys=False)
time.sleep(15)
ssh1.close()








