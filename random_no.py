# -*- coding=utf-8 -*-
# 本脚由lilaiming编写，用于学习使用！
# Email:essid@qq.com

import random
import os
import concurrent.futures


def generate_random_numbers(start, end, count):
    random_numbers = random.sample(range(start, end + 1), count)
    return sorted(random_numbers)


def generate_group_numbers(start_number, end_number, select_count, number_of_groups):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(number_of_groups):
            futures.append(executor.submit(generate_random_numbers, start_number, end_number, select_count))

        for future in concurrent.futures.as_completed(futures):
            yield future.result()


start_number = 1
end_number = 49
select_count = 6
number_of_groups = 123

# 创建保存日志的文件夹
folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'output_folder')
os.makedirs(folder_path, exist_ok=True)  # 如果文件夹已存在，则不创建

# 保存日志文件
file_path = os.path.join(folder_path, "output_log.txt")
with open(file_path, 'w') as file:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for group_number, random_numbers in enumerate(
                generate_group_numbers(start_number, end_number, select_count, number_of_groups)):
            group_output = f"第{group_number + 1}组数字: {' '.join([str(number).zfill(2) for number in random_numbers])}"
            print(group_output)
            file.write(group_output + '\n')

print(f"文件已保存至：{file_path}")
