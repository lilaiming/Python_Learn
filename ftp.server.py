# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging

# 设置日志记录
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='myftpserver.log')
ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
logger.addHandler(ch)  # 输出日志到控制台
logger.addHandler(fh)  # 输出日志到文件

# 实例化虚拟用户
authorizer = DummyAuthorizer()
authorizer.add_user("admin", "admini", "C:/Users/lilm6/Desktop", perm="elradfmw")  # 添加FTP用户
authorizer.add_anonymous("C:/Users/lilm6/Desktop")  # 添加匿名用户

# 初始化FTP处理程序
handler = FTPHandler
handler.authorizer = authorizer

# 设置被动端口范围
handler.passive_ports = range(2000, 2333)

# 设置下载上传速度限制
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024  # 300kb/s
dtp_handler.write_limit = 300 * 1024  # 300kb/s
handler.dtp_handler = dtp_handler

# 初始化FTP服务器
server = FTPServer(("0.0.0.0", 21), handler)

# 设置最大连接数
server.max_cons = 150
server.max_cons_per_ip = 15

# 启动FTP服务
server.serve_forever()





