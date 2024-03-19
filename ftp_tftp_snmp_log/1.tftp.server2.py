# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import logging
from tftpy import TftpServer

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='1.tftp.server2.log')

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 获取根日志记录器并添加控制台处理器
logger = logging.getLogger()
logger.addHandler(console_handler)

# TFTP服务器监听的IP地址和端口
server_ip = "0.0.0.0"
server_port = 69

# 服务器文件存储路径
file_path = "C:/Users/lilm6/Desktop/OS"

# 创建TFTP服务器对象
server = TftpServer(file_path)

# 启动TFTP服务器
server.listen(server_ip, server_port)
logging.info(f"TFTP server started on {server_ip}:{server_port}")

# 保持服务器运行
while True:
    pass


#交换机配置：tftp 192.168.56.1 get test123.txt
