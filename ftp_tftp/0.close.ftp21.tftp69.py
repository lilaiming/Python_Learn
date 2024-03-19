# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import subprocess

# 停止指定端口的服务器进程
def stop_server(port):
    try:
        netstat_output = subprocess.check_output(['netstat', '-ano'], encoding='gbk')
        server_pid = next((line.split()[-1] for line in netstat_output.splitlines() if f"0.0.0.0:{port}" in line), None)

        if server_pid:
            subprocess.run(['taskkill', '/pid', server_pid, '/f'])
            print(f"成功终止端口 {port} 对应的服务器进程（PID: {server_pid}）")
        else:
            print(f"未找到端口为 {port} 的服务器进程")

    except subprocess.CalledProcessError as e:
        print(f"执行命令时出错: {e}")

# 停止FTP服务器
stop_server(21)

# 停止TFTP服务器
stop_server(69)

# ###
# C:\Users\lilm6>netstat -ano|findstr 0.0.0.0:21
#   TCP    0.0.0.0:21             0.0.0.0:0              LISTENING       26348
#
# C:\Users\lilm6>taskkill -pid 26348
# 成功: 给进程发送了终止信号，进程的 PID 为 26348。
# ###

