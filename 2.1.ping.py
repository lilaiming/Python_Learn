# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import subprocess
import concurrent.futures

def ping(ip):
    # 执行ping命令
    result = subprocess.run(['ping', '-n', '4', ip], capture_output=True, text=True)

    # 检查ping结果
    if "TTL=" in result.stdout:
        # 提取平均延迟时间
        lines = result.stdout.strip().split('\n')
        avg_time = lines[-1].split(' = ')[-1].split('ms')[0]
        print(f"Ping {ip} 成功，平均延迟时间：{avg_time}ms")
        return True
    else:
        print(f"Ping {ip} 失败")
        return False

# 从文件中读取IP列表
with open('2.ip_list.txt', 'r') as f:
    ip_list = [line.strip() for line in f]

# 并发执行ping操作
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 提交每个IP的ping任务
    ping_tasks = [executor.submit(ping, ip) for ip in ip_list]

    # 等待所有任务完成
    concurrent.futures.wait(ping_tasks)

# 打印失败的IP地址列表
failed_ips = [ip for ip, task in zip(ip_list, ping_tasks) if not task.result()]
if failed_ips:
    print("以下IP ping失败：")
    for ip in failed_ips:
        print(ip)
else:
    print("所有IP均ping成功！")

