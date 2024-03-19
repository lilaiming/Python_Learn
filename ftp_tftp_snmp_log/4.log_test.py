# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import socket
import os
import datetime

def save_log(ip, log):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = f"{ip}.log"
    file_path = os.path.join(desktop_path, file_name)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {log}\n"

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(log_entry)
    else:
        with open(file_path, "w") as file:
            file.write(log_entry)

def start_log_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip, port))

    print(f"日志服务器已启动，监听 {ip}:{port} ...")

    while True:
        data, address = server_socket.recvfrom(1024)
        log_message = data.decode()
        print(f"接收到来自 {address[0]} 的日志消息：{log_message}")

        save_log(address[0], log_message)

    server_socket.close()
    print("日志服务器已停止。")

# 日志服务器配置
server_ip = '0.0.0.0'
server_port = 514

# 启动日志服务器
start_log_server(server_ip, server_port)

