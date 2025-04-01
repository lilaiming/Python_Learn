# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email: essid@qq.com

import random  # 导入随机数模块
import os  # 导入操作系统模块，用于文件和目录操作
import concurrent.futures  # 导入并发模块，用于多线程处理


def generate_random_numbers(start, end, count):
    """生成指定范围内的随机数字并返回排序后的列表。"""
    random_numbers = random.sample(range(start, end + 1), count)  # 从指定范围内随机选择指定数量的数字
    return sorted(random_numbers)  # 返回排序后的随机数字列表


def generate_group_numbers(start_number, end_number, select_count, number_of_groups):
    """生成多个随机数字组。"""
    with concurrent.futures.ThreadPoolExecutor() as executor:  # 创建线程池执行器
        futures = []  # 初始化一个空列表，用于存储未来对象
        for _ in range(number_of_groups):  # 根据指定的组数生成随机数字组
            futures.append(executor.submit(generate_random_numbers, start_number, end_number, select_count))  # 提交生成随机数字的任务

        for future in concurrent.futures.as_completed(futures):  # 遍历已完成的任务
            yield future.result()  # 逐个返回结果


start_number = 1  # 随机数字的起始范围
end_number = 49  # 随机数字的结束范围
select_count = 6  # 每组随机数字中选择的数量
number_of_groups = 10  # 需要生成的随机数字组的数量

# 创建保存日志的文件夹
folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')  # 定义文件夹路径
os.makedirs(folder_path, exist_ok=True)  # 如果文件夹已存在，则不创建

# 保存日志文件
file_path = os.path.join(folder_path, "random_no.txt")  # 定义日志文件的完整路径
with open(file_path, 'a') as file:  # 以追加模式打开文件
    with concurrent.futures.ThreadPoolExecutor() as executor:  # 创建线程池执行器
        futures = []  # 初始化一个空列表，用于存储未来对象
        for group_number, random_numbers in enumerate(  # 遍历生成的随机数字组
                generate_group_numbers(start_number, end_number, select_count, number_of_groups)):
            group_output = f"第{group_number + 1}组数字: {' '.join([str(number).zfill(2) for number in random_numbers])}"  # 格式化输出
            print(group_output)  # 输出到控制台
            file.write(group_output + '\n')  # 将结果写入日志文件

print(f"文件已保存至：{file_path}")  # 输出文件保存位置
