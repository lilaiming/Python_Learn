# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# from pyftpdlib.log import LogFormatter
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(), logging.FileHandler(filename='1.ftp.server.log')])
logger = logging.getLogger()

# 实例化虚拟用户
authorizer = DummyAuthorizer()
authorizer.add_user("admin", "admini", "C:/Users/lilm6/Desktop/OS", perm="elradfmw")  # 添加FTP用户
# authorizer.add_anonymous("C:/Users/lilm6/Desktop/OS")  # 添加匿名用户

# 初始化FTP处理程序
handler = FTPHandler
handler.authorizer = authorizer

# 设置被动端口范围
handler.passive_ports = range(2000, 2333)

# 初始化FTP服务器
server = FTPServer(("0.0.0.0", 21), handler)

try:
    # 启动FTP服务
    server.serve_forever()

except Exception as e:
    logger.error(f"Error starting FTP server: {e}")

